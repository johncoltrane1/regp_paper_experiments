import matplotlib.pyplot as plt
from plotting_utils import plotter
import os
import sys
import importlib

test_cases = [
    ["branin", "Branin"]
    ["threehumpcamelback", "ThreeHumpCamelBack"]
    ["camel_back", "CamelBack"]
    ["hartman3", "Hartman3"]
    ["hartman6", "Hartman6"]
    ["ackley4", "Ackley_4"]
    ["ackley6", "Ackley_6"]
    ["ackley10", "Ackley_10"]
    ["rosenbrock4", "Rosenbrock_4"]
    ["rosenbrock6", "Rosenbrock_6"]
    ["rosenbrock10", "Rosenbrock_10"]
    ["shekel5", "Shekel5"]
    ["shekel7", "Shekel7"]
    ["shekel10", "Shekel10"]
    ["goldsteinprice", "GoldsteinPrice"]
    ["goldstein_price_log", "GoldsteinPriceLog"]
    ["crossintray", "CrossInTray"]
    ["beale", "Beale"]
    ["dixon_price4", "DixonPrice_4"]
    ["dixon_price6", "DixonPrice_6"]
    ["dixon_price10", "DixonPrice_10"]
    ["perm4", "Perm_4"]
    ["perm6", "Perm_6"]
    ["perm10", "Perm_10"]
    ["michalewicz4", "Michalewicz_4"]
    ["michalewicz6", "Michalewicz_6"]
    ["michalewicz10", "Michalewicz_10"]
    ["zakharov4", "Zakharov_4"]
    ["zakharov6", "Zakharov_6"]
    ["zakharov10", "Zakharov_10"]
]

def get_snbo_informations():
    return {
         'GoldsteinPrice': (
            [4.630657803991099, 3.7983164376649254, 3.3914473471907387, 3.1946175970371957, 3.0976097210834204,
             3.048561197546793, 3.0242453757134506, 3.01206546161189, 3.00603828423736, 3.003011677072842,
             3.001512926516706, 3.000759534362739, 3.000377837082092, 3.0001884812600457, 3.00009386866457,
             3.000047042886999, 3.000023525365549, 3.0000153216393928, 3.00001],
            [0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05,
             1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
             4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 9.746253490447998e-09, 6.334090143442154e-09],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'GoldsteinPriceLog': (
             [1.53269893, 1.33455793, 1.22125678, 1.16146739, 1.13063076,
                    1.11466974, 1.1066616, 1.10262604, 1.10062303, 1.09961568,
                    1.09911647, 1.09886543, 1.09873823, 1.09867511, 1.09864358,
                    1.09862797, 1.09862013, 1.0986174, 1.09861562],
             [0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05,
              1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
              4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
              2.9802322387695312e-08, 1.4901161193847656e-08, 9.746253490447998e-09, 6.334090143442154e-09],
             'experiments_17_11_2021',
             'experiments_mcs_fmincon_04_01_2022',
         ),
         'Hartman3': (
            [-3.8579851379549845, -3.8597631163300554, -3.8608724128990994, -3.8615753604601646, -3.8620220288798213,
             -3.8623015616750136, -3.862479259311983, -3.8625903436402598, -3.862656869514489, -3.8627],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.2480258941650391e-07, 6.522432928085327e-08],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Hartman6': (
            [-3.0718173831021325, -3.108386498909213, -3.1384169713909396, -3.164521748720168, -3.18968144102513,
             -3.2064052912298164, -3.2217],
            [3.05169677734375e-05, 1.525848388671875e-05, 7.629241943359375e-06, 3.8146209716796874e-06,
             1.9073104858398437e-06, 1.2370052886962891e-06, 8.033359745851441e-07],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Branin': (
            [0.39947399092611224, 0.39867830766848655, 0.39828349806579944, 0.3980861023429929, 0.3979862854373053,
             0.39793648017991057, 0.3979119045001749, 0.3978996443786853, 0.3978935256175715, 0.3978904297777648,
             0.39788889350039014, 0.39788834891084324, 0.397888],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.9232630729675294e-08, 1.250544115304947e-08],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Shekel5': (
            [-3.432734952853385, -4.03563545097186, -4.685809129219841, -5.497816914881536, -6.341220350842543,
             -7.117083917101581, -7.794758852395594, -8.35991599245166, -8.813987964040933, -9.167174341278695,
             -9.436022986853157, -9.634588440295563, -9.780149221870959, -9.886499543786297, -9.962694756713326,
             -10.017914995642606, -10.056934959540841, -10.084733912353645, -10.104772094193118, -10.119023179670602,
             -10.129027214152803, -10.136080142742244, -10.141091203153376, -10.144630210009636, -10.147133259320952,
             -10.148793024717612, -10.15],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.575342119205744e-13, 5.036629954702222e-13],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Shekel7': (
            [-3.029772054726411, -3.5711842512207594, -4.177127511753282, -4.858284260507889, -5.710758506534182,
             -6.558975113705877, -7.3377400897909, -8.023077504358747, -8.590293637391312, -9.049157102048172,
             -9.408372830524844, -9.679394128560794, -9.881980096525439, -10.029487487202616, -10.135520818157278,
             -10.212264715076373, -10.267429572409878, -10.30669863771459, -10.334707917742818, -10.354584593653541,
             -10.368697713126481, -10.378628217139173, -10.38571265532401, -10.39072162318531, -10.394261149939378,
             -10.396784157383067, -10.39857312943515, -10.39985095212683, -10.400752236795192, -10.401385932495302,
             -10.401836058513114, -10.40215435287545, -10.402376323381976, -10.402534872004804, -10.40264712853447,
             -10.402725475364594, -10.402780992726672, -10.402820171352914, -10.402848064529262, -10.402867715718475,
             -10.402881675461764, -10.402891563445857, -10.402896252669262, -10.4029],
            [6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13,
             4.547473508864641e-13, 2.2737367544323206e-13, 1.1368683772161603e-13, 5.684341886080802e-14,
             2.842170943040401e-14, 1.4210854715202004e-14, 7.105427357601002e-15, 3.552713678800501e-15,
             1.7763568394002505e-15, 8.881784197001252e-16, 4.440892098500626e-16, 2.220446049250313e-16,
             1.1102230246251565e-16, 5.551115123125783e-17, 2.7755575615628914e-17, 1.792482828832931e-17,
             1.1589297729819314e-17],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Shekel10': (
            [-3.688000593866475, -4.2911901827976795, -4.992858778661498, -5.850249371476389, -6.69222752024606,
             -7.471261602720935, -8.151726721286456, -8.722563471762989, -9.178037679033935, -9.533805632102272,
             -9.806212174002077, -10.008981430185823, -10.157416330076256, -10.264813056141747, -10.342864347092721,
             -10.398801768077021, -10.438843116244453, -10.4671662762189, -10.48625509514142, -10.5],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07,
             5.960464477539063e-08, 2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09,
             3.725290298461914e-09, 1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10,
             2.3283064365386963e-10, 1.2157950550317764e-10, 6.403835713863372e-11],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Sin2': (
            [-0.8507671748132886, -0.88200106293065, -0.9028264529831376, -0.9185704181655219, -0.934919321221844,
             -0.943331547397817, -0.9475291838405567, -0.949652900874543, -0.9504931410181987, -0.951],
            [0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05,
             3.0517578125e-05, 1.8536376953125e-05, 1.1314048400878907e-05],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'CamelBack': (
            [-1.0309776951593344, -1.0313032135093771, -1.0314667688907946,
             -1.0315469011613696, -1.0315801891815792, -1.0316],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06,
             2.2483444213867186e-06, 1.3239376125335691e-06],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Rosenbrock_4': (
            [45.42394451416677, 29.653949692158385, 19.675580482633343, 13.42876145692413, 9.43280228081542, 6.832094831234983,
             5.146356772220528, 3.977691517843576, 2.9933886032559167, 2.2066254804829515, 1.6016834211923001,
             1.1506660095346932, 0.821325828077643, 0.5868419170146291, 0.41674495384636456, 0.29630834736537615,
             0.20982573397064777, 0.14941081874441767, 0.1059736109793884, 0.07494286057585903, 0.05292479543253126,
             0.03748629678469179, 0.026452688223969113, 0.018731768195077783, 0.01321570328047559, 0.009325458731847739,
             0.006576712042249298, 0.004638419315049366, 0.0032702428256719583, 0.002300122690948443, 0.0016222686569809018,
             0.001273093397565522, 0.001],
            [6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13,
             4.547473508864641e-13, 2.2737367544323206e-13, 1.1368683772161603e-13, 5.684341886080802e-14,
             3.503487278067041e-14, 2.1723022518926884e-14],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Rosenbrock_6': (
             [632.8917633859533, 452.7628161956365, 329.28960690424583, 242.7260802851347, 181.33330492822165,
              137.0253464104261, 104.0656241504697, 79.61662434741726, 61.04271701671236, 47.22884720856479, 36.763448271374884,
              28.81783952113105, 22.81106268117443, 18.279072815512727, 14.813105017220765, 12.142847141940823,
              10.089900591954253, 8.489258568864848, 7.214987482314299, 6.150535118574677, 5.19488204290412, 4.313345336721913,
              3.5415409594319343, 2.882908431236496, 2.3307968938479258, 1.873803818306444, 1.5066798509353485,
              1.2273003167153393, 1.0],
            [6.1033935546875e-05, 3.05169677734375e-05, 1.525848388671875e-05, 7.629241943359375e-06, 3.8146209716796874e-06,
             1.9073104858398437e-06, 9.536552429199219e-07, 4.7682762145996093e-07, 2.3841381072998046e-07,
             1.1920690536499023e-07, 5.9603452682495116e-08, 2.9801726341247558e-08, 1.4900863170623779e-08,
             7.4504315853118895e-09, 3.7252157926559447e-09, 1.8626078963279724e-09, 9.313039481639862e-10,
             4.656519740819931e-10, 2.3282598704099655e-10, 1.1641299352049827e-10, 5.8206496760249137e-11,
             2.9103248380124568e-11, 1.4551624190062284e-11, 7.275812095031142e-12, 3.637906047515571e-12,
             1.8189530237577855e-12, 9.094765118788928e-13, 4.806401469977572e-13, 2.550709196102398e-13],
             'experiments_17_11_2021',
             'experiments_mcs_fmincon_04_01_2022',
         ),
         'Rosenbrock_10': (
            [4918.500256153549, 3820.812536354696, 2989.9155368189518, 2355.942818965679, 1861.5446882895212,
             1482.895161876906, 1187.7898113292385, 957.3393429976702, 776.4785815260951, 632.9011043344201, 519.832286543457,
             429.11179762985284, 357.2420520339351, 298.75940459710023, 251.6387308220431, 212.9598561598246,
             181.14663581799547, 154.77926663978576, 132.99148977112858, 115.14508581601763, 100.0],
            [7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07, 4.76837158203125e-07,
             2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08, 2.9802322387695312e-08,
             1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09, 1.862645149230957e-09,
             9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10, 1.1641532182693481e-10,
             5.820766091346741e-11, 2.9103830456733704e-11, 1.4845572877675296e-11, 7.566640040022321e-12],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Ackley_4': (
            [18.44103073120918, 17.37525219290262, 16.198875003059552, 14.947822051634128, 13.675239507961876,
             12.419323482694097, 11.21021304983757, 10.072008229667013, 9.01794643751224, 8.05983670326632, 7.1848893249976165,
             6.412332858700834, 5.706731551906332, 5.140820294029648, 4.576951274980301, 4.095313725626442, 3.73017823366026,
             3.3885615758089807, 3.1082119703819715, 2.815742663285326, 2.5245946007736646, 2.2661530310544387,
             2.0224556044151787, 1.7115458137896309, 1.3918429135041515, 1.1851504303868117, 1.0],
            [0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625,
             0.0001220703125, 6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06,
             1.9073486328125e-06, 9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07,
             5.960464477539063e-08, 2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09,
             3.725290298461914e-09, 1.862645149230957e-09, 1.1175312101840973e-09, 6.689765330404043e-10],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Ackley_6': (
            [16.076844501272827, 15.250471527429077, 14.404530263744054, 13.55388159640278, 12.717998329525258,
             11.899926185696916, 11.100565545086663, 10.330349777592991, 9.601745593793328, 8.91489997323739,
             8.267820264160394, 7.656465428160668, 7.093011304760748, 6.57396717706175, 6.093552349113278, 5.652985481150427,
             5.243015830878647, 4.8803036714984955, 4.5376441468004725, 4.215443409137759, 3.9307140064348602,
             3.6809739495087386, 3.4492472896449127, 3.2374850675876226, 3.0369167165905773, 2.839685564237064,
             2.653231050595681, 2.470274766478737, 2.2797931626245647, 2.089387756900408, 1.9102609648509383,
             1.7310442027289406, 1.5329230468859358, 1.3365265109884388, 1.159438613716633, 1.0],
            [0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05,
             1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
             4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13,
             4.547473508864641e-13, 2.2737367544323206e-13, 1.1368683772161603e-13, 5.784272616438102e-14,
             2.9263213593821997e-14],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'Ackley_10': (
            [15.374008736567806, 14.864228112469572, 14.351610953091818, 13.840546426117427, 13.336301023310437,
             12.83318874470617, 12.336815307557643, 11.847281744587985, 11.366044051315363, 10.893968248890765,
             10.43902100507686, 9.993382204607386, 9.563401780551015, 9.147392751244602, 8.747916991252959, 8.360734915372637,
             7.989320166228539, 7.6350933755499755, 7.297014099833443, 6.969156091574613, 6.656592803806868,
             6.3606432381028775, 6.078959504718382, 5.810173084865234, 5.557222485762058, 5.313392837006894, 5.085447608620157,
             4.867686786720768, 4.660137829397147, 4.465125407923759, 4.277639593179186, 4.099677859230862, 3.932087997941761,
             3.774131063527483, 3.625550189872883, 3.484382693690869, 3.3497932725012256, 3.220264457300305,
             3.0946753950859933, 2.972520313037489, 2.853941779723279, 2.737430238167342, 2.622797660296277,
             2.5087264255515884, 2.3952471799978388, 2.2816745461280488, 2.169600725627897, 2.057705392348336,
             1.9454565933749852, 1.8325257226888412, 1.7204498355264932, 1.60989800983721, 1.4990869718872575,
             1.3888442562934675, 1.27807647538009, 1.1723718779464485, 1.083675936285883, 1.0],
            [7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07, 4.76837158203125e-07,
             2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08, 2.9802322387695312e-08,
             1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09, 1.862645149230957e-09,
             9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10, 1.1641532182693481e-10,
             5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11, 7.275957614183426e-12,
             3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13, 4.547473508864641e-13,
             2.2737367544323206e-13, 1.1368683772161603e-13, 5.684341886080802e-14, 2.842170943040401e-14,
             1.4210854715202004e-14, 7.105427357601002e-15, 3.552713678800501e-15, 1.7763568394002505e-15,
             8.881784197001252e-16, 4.440892098500626e-16, 2.220446049250313e-16, 1.1102230246251565e-16,
             5.551115123125783e-17, 2.7755575615628914e-17, 1.3877787807814457e-17, 6.938893903907228e-18,
             3.469446951953614e-18, 1.734723475976807e-18, 8.673617379884035e-19, 4.336808689942018e-19,
             2.168404344971009e-19, 1.0842021724855044e-19, 5.421010862427522e-20, 2.710505431213761e-20,
             1.3552527156068805e-20, 6.776263578034403e-21, 3.3881317890172014e-21, 1.6940658945086007e-21,
             8.470329472543003e-22, 4.235164736271502e-22, 2.117582368135751e-22, 1.1412498414830815e-22, 6.183519891123632e-23],
            'experiments_17_11_2021',
            'experiments_mcs_fmincon_04_01_2022',
         ),
         'ThreeHumpCamelBack': (
            [0.0006440883906866736, 0.00032281523596095233, 0.0001619978761109753, 8.072618540322371e-05,
             4.0261346749989846e-05, 2.021587743410367e-05, 1.0092764262527685e-05, 5.045555315871922e-06,
             2.512422069586164e-06, 1.2555448932941925e-06, 6.268529243706364e-07, 3.129582006029786e-07,
             1.7650886258365593e-07, 1e-07],
            [1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
             4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 4.21382486820221e-09,
             2.3790412440896035e-09],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         # 'Matyas': (
         #    [5.970517040845075e-06, 2.9730964141739207e-06, 1.4923715093851994e-06, 7.504369191679188e-07,
         #     3.743416280090282e-07, 1.8668219957984091e-07, 9.301229590337474e-08, 4.651690373915022e-08,
         #     2.335131623197325e-08, 1.1683765179348545e-08, 5.845029297300369e-09, 2.9023900104080802e-09,
         #     1.7006178471814586e-09, 1e-09],
         #    [4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
         #     2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
         #     1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
         #     1.3737240806221963e-10, 8.10016404138878e-11],
         #    'experiments_15_03_2022',
         #    'experiments_mcs_fmincon_21_03_2022',
         # ),
         'CrossInTray': (
            [-1.934414910730356, -2.0018466100746157, -2.0328970565639803, -2.0479130817448263, -2.0553116239158955,
             -2.0589616633455448, -2.0607943171663208, -2.061706807616435, -2.062157275578486, -2.062383604108015,
             -2.062498314642364, -2.0625553029215857, -2.0625836439658043, -2.062597734301655, -2.062604801425559,
             -2.0626082346808072, -2.06261],
            [0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625,
             0.0001220703125, 6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06,
             1.9073486328125e-06, 9.807586669921875e-07, 5.049435997009277e-07],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Beale': (
            [0.09297149626811346, 0.04761221784160205, 0.024159128421191917, 0.012235207938248761, 0.0061402171878751945,
             0.003067429565387009, 0.0015457810967377719, 0.0007710100105114398, 0.00038561415270872636,
             0.00019110629149611492, 9.581439448954814e-05, 4.805443762236053e-05, 2.418020539871253e-05,
             1.2104283600313773e-05, 6.082272780756422e-06, 3.0533912122428403e-06, 1.7463112471470838e-06, 1e-06],
            [0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05,
             1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
             4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             3.410220146179199e-08, 1.952044113874435e-08],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'DixonPrice_4': (
            [162.0984877203831, 89.89612167857314, 51.89822586254496, 30.06850410338067, 17.490291216688853,
             10.294368864780223, 6.144684996040142, 3.7648506353736932, 2.413436132791742, 1.6344213946823196,
             1.186495605662362, 0.9227023102382128, 0.7636022532240256, 0.6371872615881369, 0.4791049453330264,
             0.3512196183718729, 0.253803956014426, 0.18216681278571062, 0.130159974066325, 0.09257675004185142,
             0.06581256113369632, 0.04672347766650644, 0.0330609806678554, 0.023366494109820023, 0.01654820104254487,
             0.011720442546043024, 0.008287080907642772, 0.005860808646786541, 0.004152767880435306, 0.0029343956827784703,
             0.0020802935379972145, 0.001472793195200473, 0.001042172872236666, 0.0007382174405804395, 0.0005215247523924491,
             0.0003681191161623064, 0.00026034111529012356, 0.0001843560297341365, 0.00013590676028794136, 0.0001],
            [0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05,
             3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13,
             4.547473508864641e-13, 2.2737367544323206e-13, 1.1368683772161603e-13, 5.684341886080802e-14,
             2.842170943040401e-14, 1.543241978652077e-14, 8.369155574428077e-15],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'DixonPrice_6': (
            [111.40289721671844, 75.9341662636873, 51.703961852999136, 35.38996776082192, 24.32638554823238,
             16.806068409866942, 11.714993914728609, 8.252442303666768, 5.911892962335466, 4.297585572204964,
             3.1947220246865964, 2.4423802864832584, 1.9178759932265466, 1.5527996359913045, 1.2952185989351972,
             1.1131612349594096, 0.9819211183896048, 0.8812930284112697, 0.797827147119917, 0.7173856292661607,
             0.6079930730273683, 0.5],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.977729309350252e-11, 1.5220961137674748e-11],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'DixonPrice_10': (
             [850.3008792336834, 642.9298913267936, 489.6005986097217, 375.4704824340748, 290.26895255211434,
              225.09295143170766, 175.26435886038735, 137.1854930325348, 107.82846889044438, 84.9125047412721,
              66.99889996024294, 52.93238514236563, 42.01244619468724, 33.40254630914838, 26.62226297991087,
              21.311678238159395, 17.12141518783526, 13.848926263679726, 11.743916431966923, 10.0],
            [4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08,
             2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09,
             1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10,
             1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11,
             7.275957614183426e-12, 3.637978807091713e-12, 2.0946754375472663e-12, 1.206826306588482e-12],
             'experiments_15_03_2022',
             'experiments_mcs_fmincon_21_03_2022',
         ),
         'Perm_4': (
             [199.42446005482032, 82.02871913360721, 38.61895359213362, 19.071193523925963, 9.510111789005286,
                 4.754522144631284, 2.4764886444616607, 1.3964399171436168, 0.8459452808169476, 0.5375804219549496,
                 0.3555883930620647, 0.23910117155345983, 0.1625007896510525, 0.11101688473659996, 0.07567848480100764,
                 0.050670249021125366, 0.03329593015134252, 0.02141906682015633, 0.014584787616694642, 0.01],
             [0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125,
              6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
              9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07,
              5.960464477539063e-08, 3.330767154693604e-08, 1.8732234477996826e-08],
             'experiments_15_03_2022',
             'experiments_mcs_fmincon_21_03_2022',
         ),
         'Perm_6': (
            [1580986.9769695974, 417521.412360331, 111445.94796339271, 30843.176034567907, 8822.951213532651,
             2696.5253509675226, 925.2543373540443, 375.05580332911165, 184.89338435245318, 100.0],
            [0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05,
             3.0517578125e-05, 1.5958251953125e-05, 8.385423071289063e-06],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Perm_10': (
            [2.2145398423924444e+18, 5.5273814235386304e+17, 1.3876557832605094e+17, 3.4825574925414176e+16,
             8841073258787292.0, 2212462966091469.5, 551287964118377.75, 137534161941707.84, 34389418436700.08,
             8640872594721.861, 2942032492324.9966, 1000000000000.0],
            [0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125,
             6.103515625e-05, 3.0517578125e-05, 1.777069091796875e-05, 1.0393899411010743e-05],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Michalewicz_4': (
            [-3.1048964619461716, -3.234364213134053, -3.337894334329, -3.4208205142086956, -3.486860844259058,
             -3.5391829806650135, -3.5784640565317134, -3.6073051962932983, -3.628436535569624, -3.644730957750242,
             -3.6584917584783705, -3.67],
            [3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06,
             9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07,
             5.960464477539063e-08, 3.0318498611450195e-08, 1.531114498376846e-08],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Michalewicz_6': (
            [-3.1536227753080497, -3.323636026539553, -3.477755590461502, -3.6304332021197334, -3.7876696358266577,
             -3.9420185947338053, -4.0840116124739465, -4.2130953492665295, -4.33364108046967, -4.416250314570287, -4.5],
            [0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05,
             7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 1.1677169799804687e-06, 7.13498429107666e-07],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Michalewicz_10': (
            [-3.700359579501645, -3.9309331819271964, -4.149821365858372, -4.359033510675143, -4.559419904818186,
             -4.757098523028823, -4.946607312388361, -5.1285863186000125, -5.306241178012877, -5.477542588199649,
             -5.643145304797894, -5.806407928867138, -5.903639362355454, -6.0],
            [0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05,
             1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07,
             6.220531463623047e-07, 4.045273816108704e-07],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Zakharov_4': (
            [30.044662757124485, 20.423409248479, 13.90951600196139, 9.480483356315847, 6.502415298311185, 4.462625971849016,
             3.0722185670242506, 2.122203188752353, 1.472978392531585, 1.0215125885783003, 0.7153177949109464,
             0.5004959715399673, 0.3537188046486718, 0.25],
            [0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125,
             6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.871612548828125e-06,
             1.9648820846557617e-06],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Zakharov_6': (
            [118.91356256273377, 80.33845186493245, 58.4000737693008, 44.11467137042506, 34.072656070516786,
             26.541283293157388, 20.735011329963932, 16.215794814965044, 12.696244196479158, 9.937520025329375,
             7.787926280969427, 6.105350157161052, 4.785026748210575, 3.7540772783399072, 2.943974115057143,
             2.316835471557889, 1.8229253511119787, 1.4297612917096643, 1.194011059444144, 1.0],
            [0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625,
             0.0001220703125, 6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06,
             1.9073486328125e-06, 9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.4135122299194336e-07,
             8.427642617225646e-08],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         ),
         'Zakharov_10': (
            [17393.98579965569, 1301.143854635721, 267.03643077637696, 176.43818830719482, 136.98790630608153,
             110.82585075955839, 91.83175407292066, 77.20618395283617, 65.6723450060397, 57.15631066595696, 50.0],
            [0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625,
             0.00013184814453125, 7.13034765625e-05],
            'experiments_15_03_2022',
            'experiments_mcs_fmincon_21_03_2022',
         )
    }

def get_snbo_path(root, test_problem, strategy):
    sys.path.append(root)

    output = None

    for _d in os.listdir(root):
        module_loc = '{}.config'.format(_d)

        importlib.util.spec_from_file_location(module_loc)
        experiment = importlib.import_module(module_loc).method_args

        if experiment["problem_name"] != test_problem:
            continue

        if experiment["model"][0] == "gp":
            if strategy == "None":
                assert output is None
                output = _d

        if experiment["model"][0] == "gp_slacked":
            q_dicts = experiment["model"][1]["q_dicts"]
            if len(q_dicts) != 1:
                continue
            if list(q_dicts.items())[0][0] == "q_init-0.25":
                if strategy == "Constant":
                    assert output is None
                    output = _d
            if list(q_dicts.items())[0][0] == "q-0.25":
                if strategy == "Concentration":
                    assert output is None
                    output = _d

    return os.path.join(root, output)

def plot_case(test_problem_gpmp, test_problem_snbo, root_gpmp, root_snbo, output_dir, figsize=(3.0, 2.6)):
    root_snbo = os.path.join(root_snbo, get_snbo_informations()[test_problem_snbo][2])

    plotter(
        {
            "ConcentrationNew": [os.path.join(root_gpmp, test_problem_gpmp, "Concentration"),('orange', 'dashed')],
            "ConstantNew": [os.path.join(root_gpmp, test_problem_gpmp, "Constant"), ('blue', 'dashed')],
            "NoneNew": [os.path.join(root_gpmp, test_problem_gpmp, "None"), ('green', 'dashed')],
            "Concentration": [get_snbo_path(root_snbo, test_problem_snbo, "Concentration"), ('orange', 'solid')],
            "Constant": [get_snbo_path(root_snbo, test_problem_snbo, "Constant"), ('blue', 'solid')],
            "None": [get_snbo_path(root_snbo, test_problem_snbo, "None"), ('green', 'solid')],
        },
        306,
        test_problem_snbo,
        100,
        figsize=figsize
    )

    plt.save(os.path.join(output_dir, test_problem_gpmp))

for test_case in test_cases:
    plot_case(
        test_case[0],
        test_case[1],
        root_gpmp,
        root_snbo,
        output_dir,
        figsize=(3.0, 2.6)
    )