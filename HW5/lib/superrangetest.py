import random
from myrandom import Myrandom
from num import Numb
from range import Range
# import range
from superrange import Superrange
import config

the = config
R = Myrandom()
RANGE = Range()
SUPER = Superrange()

def x(z):
    return z[0]


def y(z):
    return z[-1]


def klass(z):
    if z < 0.2:
        return 0.2 + 2 * R.r() / 100
    elif z < 0.6:
        return 0.6 + 2 * R.r() / 100
    else:
        return 0.9 + 2 * R.r() / 100


def main():
    t = []
    n = Numb()
    for _ in range(1, 50):
        #w = random.random()
        w = R.r()
        kla = klass(w)
        n.update(kla)
        t.append([w, kla])
    # print(t)
    # t = [[0.35115619678976784, 0.6073067734145126], [0.0243789038058293, 0.2025073075119906], [0.819487326041709, 0.9018392978151512], [0.9103757993164581, 0.9049407777120083], [0.6236596242480225, 0.9047554886735769], [0.6522986469274215, 0.9014537176589732], [0.2038387997697847, 0.6130783792459771], [0.425574088788203, 0.6001539637242229], [0.43555833673159217, 0.6010692327008905], [0.660985480981625, 0.9033301440083097], [0.07560956668900243, 0.2010016796742574], [0.8969922490158013, 0.909173002638469], [0.5297875915600219, 0.6095546353000936], [0.4773866454024389, 0.6054541993352837], [0.40242279086823807, 0.6070203049606738], [0.45925370779344676, 0.6055416360057618], [0.987889477279127, 0.905498136806068], [0.48907250800005064, 0.6147244902861884], [0.4552061261664264, 0.6180930618467243], [0.9582438410267189, 0.916830212789043], [0.9777925619271532, 0.9105940038667033], [0.5287760037347395, 0.6083497194891561], [0.4899019339974937, 0.6014749815042479], [0.07051446983452847, 0.21661930692224732], [0.7637626489502478, 0.9135859281167322], [0.2779871016245544, 0.6053863454448927], [0.1284083312517177, 0.2000001565273852], [0.7406324769122553, 0.9083078923115078], [0.14370950542525918, 0.21511210644390066], [0.029833194275888708, 0.21895528499919703], [0.23960882494053515, 0.6046638975686691], [0.9431272865945608, 0.9186087298945564], [0.2846870561702557, 0.6035665540786304], [0.9379406701081475, 0.9182064166097932], [0.49832608596429107, 0.6178147496272878], [0.13607052657198637, 0.20638065882324272], [0.09381808482260767, 0.20307439954163248], [0.8064795736250477, 0.9053228901444575], [0.26040055487110325, 0.6151282097190284], [0.9479460554406425, 0.907716294074299], [0.6903139283433525, 0.9099696023808651], [0.8002041168981552, 0.9030067011914248], [0.6692514853712905, 0.9097303476602446], [0.7512586524144484, 0.900317354025467], [0.2809205193465635, 0.6179531257310664], [0.26606287729275035, 0.6191072151992038], [0.9873382880925372, 0.9110916769649329], [0.7331879801390035, 0.9029506600661905], [0.8164147921061932, 0.9169196312022021]]
    print("{}".format("\nWe have many unsupervised ranges."))
    for j, one in enumerate(RANGE.function(t, x)):
        print(" x\t{} [span={} lo={} n={} hi={}]".format(j, one.span, one.lo, one.n, one.hi))
    print("{}".format("\nWe have fewer supervised ranges."))
    for j, one in enumerate(SUPER.function(t, x, y)):
        print(" super\t{} [label={} most={} ]".format(j, one.label, one.most))
    pass


if __name__ == "__main__":
    R.seed(1)
    main()