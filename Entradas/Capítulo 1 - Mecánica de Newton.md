## Leyes de Newton

1. Un punto material aislado permanece en un movimiento rectilíneo uniforme en sistemas de referencia inerciales.
2. Se define como una fuerza sobre un cuerpo a una interacción que modifica su movimiento. Esta interacción es, por definición, proporcional a la aceleración, con $$\mathbf F = m \mathbf {\ddot r}.$$ La constante de proporcionalidad es la masa inercial.
3. Cuando dos partículas interactúan, la fuerza que la primera ejerce sobe la segunda es igual en intensidad y dirección, pero opuesta en sentido, a la que la segunda ejerce sobre la primera.

## Transformación de Galileo

Cambio de un sistema de referencia inercial. Si $S'$ se mueve a $\mathbf U$ respecto de $S$, entonces:
$$
\mathbf x' = \mathbf x - \mathbf U t
$$
según Galileo. Dado que las leyes de Newton son invariantes (tienen la misma forma) en todos los sistemas inerciales, entonces las masas y las fuerzas también deben ser invariantes frente a estas transformaciones. 

## Sistema de varias partículas

### Impulso lineal

Definimos como *cantidad de movimiento* o *impulso lineal* total de un sistema de partículas:
$$
\mathbf P = \sum_{i=1}^{N} \mathbf{p}_i
$$
donde $\mathbf p_i = m_i \dot {\mathbf x}_i$ es la cantidad de movimiento de la partícula $i$. La variación de $\mathbf P$ está dada por la segunda ley de Newton:
$$
\frac{d \mathbf P}{d t} = \sum_{i=1}^{N} \frac{d \mathbf p_i}{dt} = \sum_{i=1}^{N} \mathbf F_{i}^{\text{ext}} + \sum_{i=1}^{N} \sum_{j \neq i} \mathbf f_{ij} 
$$
Por la tercera ley de Newton, $\mathbf f_{ij} = -\mathbf f_{ji}$, así que se anula el término de la doble sumatoria, y se tiene:

$$
\boxed{\frac{d \mathbf P}{dt} = \mathbf F_{\text{neta}}^{\text{ext}}}
$$

{#eq:cap1_dPdt}

### Centro de masa

Es útil considerar el centro de masa del sistema:
$$
\mathbf X_{\text{CM}} = \frac{1}{M} \sum_{i=1}^N  m_i \mathbf x_i
$$
donde $M$ es la masa total. De esta forma, 
$$
\mathbf P = M \mathbf X_{\text{CM}}
$$
Y se tiene como equivalente a la @eq:cap1_dPdt la ecuación de movimiento del centro de masas:
$$
M\frac{d^2 \mathbf X_{\text{CM}}}{dt^2} = \mathbf{F_{\text{neta}}^{\text{ext}}}
$$

### Momento angular


