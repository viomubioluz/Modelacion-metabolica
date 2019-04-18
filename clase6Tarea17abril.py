import cobra
def funcion():
    model2= cobra.io.read_sbml_model ("e_coli_core.xml")


print len(model2.reactions)
print len(model2.metabolites)
print model2.objective

solution = model2.optimize()

model2.summary()


for reaction in model2.metabolites.get_by_id('glc__D_e').reactions:
    print reaction.id, reaction.bounds
    
    

model2.reactions.get_by_id("EX_glc__D_e").bounds=(-1,1000)
solution = model2.optimize()
model2.summary()


solution = model2.optimize()
model2.summary()



from cobra.flux_analysis import flux_variability_analysis
fva=flux_variability_analysis(model2)


print model2.metabolites.get_by_id('glc__D_e').reactions
print "value"
print fva.loc['EX_glc__D_e']


solution = model2.optimize()
model2.summary(fva=1)



#PARSIMONIA FBA


fba2_solution = model2.optimize()

pfba2_solution = cobra.flux_analysis.pfba(model2)


fba2_solution = model2.optimize()

pfba2_solution = cobra.flux_analysis.pfba(model2)
print fba2_solution.objective_value
print pfba2_solution.objective_value


print fba2_solution.fluxes["BIOMASS_Ecoli_core_w_GAM"]
print pfba2_solution.fluxes["BIOMASS_Ecoli_core_w_GAM"]
print abs(fba2_solution.fluxes["BIOMASS_Ecoli_core_w_GAM"] - pfba2_solution.fluxes["BIOMASS_Ecoli_core_w_GAM"])


print sum(fba2_solution.fluxes)
print sum(pfba2_solution.fluxes)

return  