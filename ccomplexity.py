from radon.complexity import cc_rank, cc_visit
import radon.cli.harvest as harvest
from radon.cli import Config

def print_pub_complexity(filename):
    
    with open(filename, 'r') as file:
        source_code = file.read()

    # calculate complexity
    blocks = cc_visit(source_code)

    # print complexity
    for block in blocks:
        complexity_score = block.complexity
        rank = cc_rank(complexity_score)
        print(f"Functia {block.name} are complexitatea ciclomatica {complexity_score} (Rank: {rank})")

if __name__ == '__main__':
    source_file_path = 'pub.py'
    print_pub_complexity(source_file_path)

