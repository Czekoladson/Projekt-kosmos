

class Stats():
    def __init__(self,ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False    # Do naprawy gra i tak startuje

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit