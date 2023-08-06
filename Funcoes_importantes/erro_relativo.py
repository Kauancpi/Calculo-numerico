from numpy import fabs


def erro_percentual(raiz_encontrada,raiz_real):
    return(100*fabs(raiz_encontrada-raiz_real)/fabs(raiz_real))