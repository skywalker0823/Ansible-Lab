import ansible.runner
import sys

runner = ansible.runner.Runner(
    module_name='shell',
    module_args='ls',
    pattern='localhost',
    forks=10
)

datastructure = runner.run()