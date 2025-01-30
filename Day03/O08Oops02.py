
class Player:

    def __init__(self):
        print("Player initialized.....")

    def get_runs(self):
        print("runs scored.....")

    def __del__(self):
        print("Object destroyed.....")

sachin = Player()
rahul = Player()

print("-" * 60)
sachin.__init__()
sachin.get_runs()
rahul.get_runs()

print("-" * 60)
del sachin
print("-" * 60)
