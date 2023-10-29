from re import X
from sklearn import covariance
from src.jeuDomino import *
from src.statistic import Statistic
from src.viewer import Viewer

stat = Statistic(JeuDomino(7), Viewer())

### Loi de probabilité
loi_X = stat.loi_de_probabilite(stat.get_X(), stat.NOMBRE_DE_LANCER)
# stat.viewer.loi_de_probabilite(loi_X)
loi_Y = stat.loi_de_probabilite(stat.get_Y(), stat.NOMBRE_DE_LANCER)
# stat.viewer.loi_de_probabilite(loi_Y)

### Fonction de repartition
repartition_X = stat.fonction_de_repartition(loi_X)
# stat.viewer.fonction_de_repartition(repartition_X)
repartition_Y = stat.fonction_de_repartition(loi_Y)
# stat.viewer.fonction_de_repartition(repartition_Y)

### Espérance 
esperance_x = stat.esperance(stat.get_X(), stat.NOMBRE_DE_LANCER)
esperance_y = stat.esperance(stat.get_Y(), stat.NOMBRE_DE_LANCER)
esperance_z = stat.esperance(stat.get_Z(), stat.NOMBRE_DE_LANCER)
print("\nESPERANCE")
print("\tEsperance x : ", esperance_x)
print("\tEsperance y : ", esperance_y)
print("\tEsperance z : ", esperance_z)

### Variance
var_x = stat.variance(stat.get_X(), esperance_x, stat.NOMBRE_DE_LANCER)
var_y = stat.variance(stat.get_Y(), esperance_y, stat.NOMBRE_DE_LANCER)
print("\nVARIANCE")


print("\tVariance x : ", var_x)
print("\tVariance y : ", var_y)

### Autres statistiques
print("\nAUTRES STATS")
print("\tProbabilité de succés : ", stat.proba_succes())
print("\tMediane : ", stat.median_point_restant())

### Nuage de point
# stat.viewer.nuage_de_point(stat.get_X(), stat.get_Y())

### Covariance

cov_xy = stat.covariance(esperance_z, esperance_x, esperance_y)
ecart_type_x = stat.ecart_type(stat.get_X(), esperance_x, stat.NOMBRE_DE_LANCER)
ecart_type_y = stat.ecart_type(stat.get_Y(), esperance_y, stat.NOMBRE_DE_LANCER)

coefficient_correlation = stat.coefficient_de_correlation(cov_xy, ecart_type_x, ecart_type_y)
print("\nCOVARIANCE ET COEFFICIENT DE CORRELATION")
print("\tCovariance : ", cov_xy)
print("\tCoefficient correlation : ", coefficient_correlation)
print("\tEcart-type X : ", ecart_type_x)
print("\tEcart-type Y : ", ecart_type_y)


