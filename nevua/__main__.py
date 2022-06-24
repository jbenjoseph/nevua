import importlib
from fire import Fire


class Controller:
    def up(self, debug=False):
        """
        Run the web application and build the cache if needed.
        """
        import nevua.app as app

        app.main(debug)

    def cache(self, hp=None):
        """
        Just cache the data. It doesn't run the web app.
        """
        from nevua.app import process_data

        if hp:
            print(f"Hyperparameters: {hp}")
            process_data(hp=hp)
        else:
            process_data()

    if importlib.util.find_spec("sigopt"):

        def new_experiment(self, apikey):
            """
            Create a new SigOpt experiment.
            """
            from nevua.extras.optim import create_experiment

            print(create_experiment(apikey))

        def continue_experiment(self, apikey, exp_id):
            """
            Continue running a SigOpt experiment.
            """
            from nevua.extras.optim import continue_experiment

            continue_experiment(apikey, exp_id)

        def clean_experiment(self, apikey, exp_id):
            """
            Remove any dangling state from a SigOpt experiment.
            """
            from nevua.extras.optim import clean_experiment

            clean_experiment(apikey, exp_id)


def main():
    Fire(Controller)
