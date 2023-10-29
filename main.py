from sklearn import covariance
from src.jeuDomino import *
from src.statistic import Statistic
from src.viewer import Viewer

stat = Statistic(JeuDomino(7), Viewer())
stat.viewer.nuage_de_point(stat.get_X(), stat.get_Y())

esperance_x = stat.esperance(stat.get_X(), stat.NOMBRE_DE_LANCER)
esperance_y = stat.esperance(stat.get_Y(), stat.NOMBRE_DE_LANCER)
esperance_z = stat.esperance(stat.get_Z(), stat.NOMBRE_DE_LANCER)

cov_xy = stat.covariance(esperance_z, esperance_x, esperance_y)
ecart_type_x = stat.ecart_type(stat.get_X(), esperance_x, stat.NOMBRE_DE_LANCER)
ecart_type_y = stat.ecart_type(stat.get_Y(), esperance_y, stat.NOMBRE_DE_LANCER)

coefficient_correlation = stat.coefficient_de_correlation(cov_xy, ecart_type_x, ecart_type_y)
print(coefficient_correlation)