Residuals (Residuos):
    La sección resume los residuos, el error entre la predicción del modelo y los resultados reales. Los residuos más pequeños son mejores.
Coefficients (Coeficientes):
    Para cada variable y la intersección, se produce una ponderación y esa ponderación tiene otros atributos como el error estándar, un valor de prueba t y significación.
    Estimación:
        Este es el peso dado a la variable. En el caso de regresión simple (una variable más la intersección), por cada aumento de un dólar en el gasto, el modelo predice un aumento de $ 10.6222.
    Std. Error:
        Le indica con qué precisión se midió la estimación. Realmente solo es útil para calcular el valor t.
    Valor t y Pr (> [t]):
        El valor t se calcula tomando el coeficiente dividido por el Std. Error. Luego se usa para probar si el coeficiente es significativamente diferente de cero. Si no es significativo, entonces el coeficiente realmente no agrega nada al modelo y podría descartarse o investigarse más a fondo. Pr (> | t |) es el nivel de significancia.
Signif. codes (Medidas de rendimiento):
    Se proporcionan tres conjuntos de medidas.
Residual standard error(Error estándar residual):
    Esta es la desviación estándar de los residuos. Más pequeño es mejor.
Multiple R-squared (Cuadrado R múltiple / ajustado):
    Para una variable, la distinción realmente no importa. R-cuadrado muestra la cantidad de varianza explicada por el modelo. R-Square ajustado tiene en cuenta el número de variables y es más útil para la regresión múltiple.
F-statistic (Estadística F):
    La prueba F verifica si el peso de al menos una variable es significativamente diferente de cero. Esta es una prueba global para ayudar a evaluar un modelo. Si el valor p no es significativo (por ejemplo, mayor que 0.05), su modelo esencialmente no está haciendo nada.