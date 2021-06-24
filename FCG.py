from pyomo.environ import *
from pyomo.opt import SolverFactory
import numpy as np
from distMat import getDist
from pathlib import Path



def FCG_instance(data):   # data= file path
    
    dist=getDist(data)  # load distance (cost) matrix
    
    model=ConcreteModel()
    
    n=len(dist)
    model.v=RangeSet(n)
    model.c=Param(model.v,model.v,initialize=lambda model, i, j: dist[i-1,j-1])
    
    model.x=Var(model.v,model.v,domain=Binary)
    model.y=Var(model.v,model.v,domain=NonNegativeReals)
    model.z=Var(model.v,model.v,domain=NonNegativeReals)
    
    #### constraints
    
    model.v2=RangeSet(2,n)

    model.cons1= Constraint(model.v,rule=lambda model, j: sum(model.x[i,j] for i in model.v) == 1)
    model.cons2= Constraint(model.v,rule=lambda model, i: sum(model.x[i,j] for j in model.v) == 1)
    model.cons3= Constraint(model.v,rule=lambda model: sum(model.y[1,j] for j in model.v) - sum(model.y[j,1] for j in model.v) == n-1)
    model.cons4= Constraint(model.v2,rule=lambda model, i: sum(model.y[i,j] for j in model.v) - sum(model.y[j,i] for j in model.v) == -1)
    model.cons5= Constraint(model.v,rule=lambda model: sum(model.z[1,j] for j in model.v) - sum(model.z[j,1] for j in model.v) == 1-n)
    model.cons6= Constraint(model.v2,rule=lambda model, i: sum(model.z[i,j] for j in model.v) - sum(model.z[j,i] for j in model.v) == 1)
    model.cons7= Constraint(model.v,rule=lambda model, i: sum(model.y[i,j] for j in model.v) + sum(model.z[i,j] for j in model.v) == n-1)
    model.cons8= Constraint(model.v, model.v,rule=lambda model, i ,j: model.y[i,j] + model.z[i,j] == (n-1)*model.x[i,j])
  
    
    ###optimization problem
    
    model.obj = Objective(rule=lambda model: sum(model.x[i,j] * model.c[i,j] for i in model.v for j in model.v),sense=minimize)
    
    return model


def solve_FCG(data):
    
    model=FCG_instance(data)
    opt = SolverFactory("glpk")
    results = opt.solve(model)
    
    print("\displaying Solution\n" + '-'*60)
    results.write()
    return  model.x.display(), model.obj.display()
