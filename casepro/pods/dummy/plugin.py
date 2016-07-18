from casepro.pods import Pod, PodConfig, PodPlugin


class DummyPodConfig(PodConfig):
    pass


class DummyPod(Pod):
    def read_data(self, params):
        pass


class DummyPodPlugin(PodPlugin):
    label = 'dummy_pod'
    pod_class = DummyPod
    config_class = DummyPodConfig
    title = 'Dummy Pod'
