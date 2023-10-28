from src.jeuDomino import *
from src.Statistic import Statistic

stat = Statistic(JeuDomino(7))
print(stat.variance(stat.tab_val_y, stat.esperance(stat.tab_val_y, stat.NOMBRE_DE_LANCER), stat.NOMBRE_DE_LANCER))
print(stat.ecart_type(stat.tab_val_y, stat.esperance(stat.tab_val_y, stat.NOMBRE_DE_LANCER), stat.NOMBRE_DE_LANCER))
print(stat.proba_succes())
print(stat.median_point_restant())