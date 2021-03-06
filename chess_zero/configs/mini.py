"""
Contains the set of configs to use for the "mini" version of the app, which seems to be a smaller
version of the agent that is easier and quicker to run locally
"""
class EvaluateConfig:
    def __init__(self):
        self.vram_frac = 1.0
        self.game_num = 120
        self.replace_rate = 0.55
        self.play_config = PlayConfig()
        self.play_config.simulation_num_per_move = 200 # 200
        self.play_config.thinking_loop = 1
        self.play_config.c_puct = 1 # lower  = prefer mean action value
        self.play_config.tau_decay_rate = 0.09 # I need a better distribution...
        self.play_config.noise_eps = 0
        self.evaluate_latest_first = True
        self.max_game_length = 1000


class PlayDataConfig:
    def __init__(self):
        self.min_elo_policy = 500 # 0 weight
        self.max_elo_policy = 1800 # 1 weight
        self.sl_nb_game_in_file = 250
        self.nb_game_in_file = 100
        self.max_file_num = 150


class PlayConfig:
    def __init__(self):
        self.max_processes = 3 # 3
        self.search_threads = 16 # 16
        self.vram_frac = 1.0
        self.simulation_num_per_move = 150 # 100
        self.thinking_loop = 1
        self.logging_thinking = False
        self.c_puct = 1.1 # 1.5
        self.noise_eps = 0.05 # 0.25
        self.dirichlet_alpha = 0.6
        self.tau_decay_rate = 0.32 # 超过12回合，tau为0；0.32
        self.virtual_loss = 3 # 没有什么影响
        self.resign_threshold = -0.8
        self.min_resign_turn = 5
        self.max_game_length = 1000


class TrainerConfig:
    def __init__(self):
        self.min_data_size_to_learn = 0
        self.cleaning_processes = 5 # RAM explosion...
        self.vram_frac = 1.0
        self.batch_size = 512 # 384
        self.epoch_to_checkpoint = 1
        self.dataset_size = 1500000
        self.start_total_steps = 0
        self.save_model_steps = 25
        self.load_data_steps = 100
        self.loss_weights = [1.25, 1.0] # [policy, value] prevent value overfit in SL
        self.dropout = 0.5

class ModelConfig:
    cnn_filter_num = 256
    cnn_first_filter_size = 5
    cnn_filter_size = 3
    res_layer_num = 4
    l2_reg = 1e-4
    value_fc_size = 256
    distributed = False
    input_depth = 18
