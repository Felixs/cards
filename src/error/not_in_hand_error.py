class NotInHandError(Exception):

    def __init__(self, card: str):
        self.card = card
        self.message = f"Card '{card}' not found in player hand!"
        super().__init__(self.message)
