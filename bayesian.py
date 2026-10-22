from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Rain', 'WetGrass')])

rain = TabularCPD('Rain', 2, [[0.7], [0.3]])
wet = TabularCPD('WetGrass', 2,
                 [[0.9, 0.2], [0.1, 0.8]],
                 evidence=['Rain'], evidence_card=[2])

model.add_cpds(rain, wet)
infer = VariableElimination(model) 
print(infer.query(['WetGrass']))
