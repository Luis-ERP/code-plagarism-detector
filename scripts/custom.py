import os

from algorithm import Algorithm
from utlis import findOccurrences, extractNumber


class CustomAlgorithm(Algorithm):
    def __init__(self, version: int, quiet: bool) -> None:
        Algorithm.__init__(self, 'custom', version, quiet)
        self.EXE_PATH: str = os.path.join('resources', 'custom', 'custom.py')

    def _run_on_pair(self, pair: str) -> None:
        f1, f2 = pair.split('_')
        file1 = os.path.join(self.DATASET_DIR, pair, f'{f1}.java')
        file2 = os.path.join(self.DATASET_DIR, pair, f'{f2}.java')

        gen_pair_dir = os.path.join(self.GEN_DIR, pair)
        os.makedirs(gen_pair_dir, exist_ok=True)

        pair_report = os.path.join(gen_pair_dir, f'{f1}_{f2}.txt')

        cmd = f'python {self.EXE_PATH} -p {file1} {file2} > {pair_report}'
        os.system(cmd)

    def _get_pair_similarity(self, pair: str) -> float:
        def get_percent_number(file):
            with open(file, 'r') as pair_report:
                text = pair_report.read()
            # occs is empty <-> file1, file2 have no same tokens
            occs = findOccurrences(text, "%")
            return float(extractNumber(text, occs[0])) if occs else 0.0

        gen_pair_dir = os.path.join(self.GEN_DIR, pair)
        f1, f2 = pair.split('_')
        result = get_percent_number(os.path.join(gen_pair_dir, f'{f1}_{f2}.txt'))

        return result
    