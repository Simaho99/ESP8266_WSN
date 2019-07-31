import random

"""WSN nodes consist of several functional modules: Micro- processor, Transceiver,
Sensor, and power supply modules as shown on readme.By studying the energy consumption
issues of node components in different component states and during state transitions,
this section presents the energy models of the processor module, communication module
and sensing module of WSN nodes, and then establishes the node energy model by adopting
the event-driven mechanism"""


class Parameters(object):
    """
    CPU parameters
    op_state = (run, idle, sleep) operation state of the CPU in mW
    trans_state = (run-idle, idle-run, idle-sleep, run-sleep, sleep-run) time for
    transition changes from one operation to another in microseconds
    TODO:
    Tcpu_state is the time interval in state i which is a statistical variable that
    can be calculated in this processor energy model.
    A function of bitrate??

    """
    def __init__(self, node_id):
        self.node_id = node_id

    def op_state(self, op_=(400, 50, 0.16)):
        op = op_
        return op, self.node_id

    def trans_state(self, tr_=(90, 90, 90, 10, 10)):
        tr = tr_
        return tr, self.node_id

    def tcpu(self, tcpu_=(90, 90, 90, 10, 10)):

        return tcpu_, self.node_id

    def p_init(self, p_init_=(90, 90, 90, 10, 10)):

        return p_init_, self.node_id

    def node_parameters(self):
        return self.op_state(), self.trans_state(), self.tcpu(), self.p_init()





class PowerSupply(Parameters):                                          # Power Supply module
    def __init__(self):
        super().__init__()


class Tranceiver(object):                                           # Tranceiver module
    def __init__(self):
        pass


class Sensor(object):                                               # Sensor module
    def __init__(self):
        pass


class Processor(Parameters):                                            # Processor module
    """the processor has theree states, running, idle and sleeping. During that time the
    processor consumes the different values of power. The processor also have five
    transmission stages as shown on figure one on the attached document"""
    def __init__(self):
        super().__init__()

    def energy_cpu(self):
        """is the sum of the energy consumption and state-transition energy consumption
        Ecpu = Ecpu-state + Ecpu-change"""

        for i in range(0, len(self.op_state)):
            E_cpu = self.op_state[i]*self.Tcpu                  #TODO: check the Tcpu issue
            E_cpu_change = self.trans_state[i]*Pinit

        pass

class Energy(PowerSupply, Tranceiver, Sensor, Processor):           # Default total energy
    def __init__(self):
        super().__init__()





