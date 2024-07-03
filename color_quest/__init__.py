from matplotlib import pyplot as plt
import numpy as np

def show_color():
    """
    show a figure with random face color and return the color in tuple[int]

    Input:
        None
    Output:
        (tuple[int, int, int]) : 8bit RGB values' color
    """
    rg = np.random.default_rng()
    rgb_array = rg.integers(low=0, high=255, size=3)
    rgb = tuple([int(e) for e in rgb_array])
    rgb_norm = tuple([e / 256 for e in rgb])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor(rgb_norm)
    fig.show()
    return rgb

def rgb_to_hex(rgb:tuple[int]):
    """
    convert RGB tuple to hexadecimal code

    Input:
        rgb (tuple[int,int,int]) : 8bit RGB values
    Output:
        hexadecimal code (str)
    """
    return '#%02x%02x%02x' % rgb

def answer_rgb(trials,dists):
    """
    return RGB tuple from STDIN written as "128,32,255"

    Input:
        trials (list[tuple[int]]) : rgb-tuples trials
        dists (list[float]) : distances returned against for trials
    Output:
        next trial RGB tuple
    """
    rgb_str = input()
    rgb = tuple(int(a) for a in rgb_str.split(","))
    return rgb

class Quest():
    def __init__(self):
        self.rgb_truth = show_color()
        self.n = 0
        self.trials = list()
        self.dists = list()
    def quest(self):
        print(f'Trial #{self.n}')
        print(f'\t (R,G,B)?')
    def eval(self,rgb_trial):
        self.n += 1
        return np.sqrt(np.sum((np.array(rgb_trial) - np.array(self.rgb_truth)) ** 2))

def main(f=answer_rgb):
    Q = Quest()
    trials = list()
    dists = list()
    while len(trials) <= 20:
        Q.quest()
        rgb_trial = f(trials,dists)
        d = Q.eval(rgb_trial)
        print(f"-> your answer: {rgb_to_hex(rgb_trial)}")
        print(f"-> error: {d=}")
        if d < 1:
            break
        else:
            trials.append(rgb_trial)
            dists.append(d)
    print(f"you tried {n} times!")
    print(f'truth: {rgb_to_hex(Q.rgb_truth)} {Q.rgb_truth}')

if __name__ == "__main__":
    main()
