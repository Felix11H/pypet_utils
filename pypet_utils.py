
from pypet import load_trajectory
from pypet.brian2.parameter import Brian2Parameter, \
                                   Brian2MonitorResult

def load_trajectories(filename, brian2=True):

    loading, idx = True, 0
    trajectories = []

    while loading:

        if brian2:
            tr = load_trajectory(index=idx, filename=filename,
                                 dynamic_imports=[Brian2MonitorResult,
                                             Brian2Parameter])
        else:
            tr = load_trajectory(index=idx, filename=filename)
        trajectories.append(tr)
        
        idx += 1

        try:
            if brian2:
                tr = load_trajectory(index=idx, filename=filename,
                                     dynamic_imports=[Brian2MonitorResult,
                                                 Brian2Parameter])
            else:
                tr = load_trajectory(index=idx, filename=filename)

        except ValueError:
            loading=False


    return trajectories


def contained_trajectories(filename, brian2=True):
    trs = load_trajectories(filename, brian2)
    return [tr.name for tr in trs]
