from matplotlib import pyplot as plt
import numpy as np

def show_color():
    rg = np.random.default_rng()
    rgb = rg.integers(low=0, high=255, size=3)
    rgb_norm = tuple([e / 256 for e in rgb])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor(rgb_norm)
    fig.show()
    return rgb

# convert RGB tuple to hexadecimal code
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def answer_rgb(rgb_tuple):
    rgb_str = input()
    rgb = tuple(int(a) for a in rgb_str.split(","))
    return rgb


def main(f=answer_rgb):
    rgb_truth = show_color()
    n = 1
    d = 255 * np.sqrt(3)
    rgb_trial0 = (0,0,0)
    while True:
        print(f"Trial #{n}")
        print(f"-> (R,G,B)?")
        rgb_trial = f(rgb_trial0)
        print(f"-> your answer: #{rgb_to_hex(rgb_trial)}")
        d = np.sqrt(np.sum((rgb_trial - rgb_truth) ** 2))
        if d < 1:
            break
        else:
            print(f"-> error: {d=}")
            rgb_trial0 = rgb_trial
            n += 1
    print(f"you tried {n} times!")

if __name__ == "__main__":
    main()
