
¡Excelente pregunta! Esta tabla es el **ABC del Análisis Exploratorio de Datos (EDA)**. Son las primeras tareas que todo científico de datos hace al recibir un dataset nuevo. Vamos a desglosar cada una para que entiendas **qué hace, por qué es importante y cómo interpretar los resultados**.

---

### 1. Ver valores faltantes: `df.isna().sum()`

**¿Qué hace?**
- `df.isna()`: Crea una "máscara" o copia del DataFrame donde cada celda es `True` (si el valor es faltante: `NaN`, `None`) o `False` (si tiene un valor).
- `.sum()`: Como en Python `True` vale 1 y `False` vale 0, al sumar cada columna, obtienes el **total de valores faltantes** por columna.

**¿Por qué es importante?**
Los valores faltantes sesgan tus análisis y muchos algoritmos de Machine Learning no funcionan con ellos. Debes saber cuántos tienes y en qué columnas para decidir si los eliminas, los imputas (rellenas con un valor como la media), etc.

**Ejemplo de salida:**
```
Nombre          0
Edad            2
Calificación    1
dtype: int64
```
**Interpretación:** La columna 'Edad' tiene 2 valores faltantes y 'Calificación' tiene 1. 'Nombre' está completo.

---

### 2. Ver duplicados: `df.duplicated().sum()`

**¿Qué hace?**
- `df.duplicated()`: Busca filas que sean **exactamente iguales** a otra fila anterior en el DataFrame. Marca la primera aparición como `False` y las copias como `True`.
- `.sum()`: Cuenta cuántas de estas filas duplicadas (`True`) existen.

**¿Por qué es importante?**
Los duplicados inflan artificialmente tu dataset. Si tienes 1000 filas pero 100 son duplicados, en realidad solo tienes 900 observaciones únicas. Esto distorsiona los resultados de tus análisis y modelos.

**Ejemplo de salida:**
```
5
```
**Interpretación:** Hay 5 filas en tu dataset que son copias exactas de otras.

---

### 3. Tipos de columna: `df.dtypes`

**¿Qué hace?**
Te muestra el **tipo de dato** que Pandas ha inferido para cada columna.

**¿Por qué es importante?**
- **Correcto análisis:** No puedes calcular la media de una columna de texto (`object`).
- **Eficiencia de memoria:** Usar el tipo correcto (ej. `int32` vs `int64`) ahorra memoria.
- **Problemas comunes:** A veces una columna numérica se lee como texto (`object`) porque tiene un símbolo como "$" o una coma. Esto lo detectas aquí.

**Ejemplo de salida:**
```
Nombre          object
Edad             int64
Calificación   float64
dtype: object
```
**Interpretación:** 'Nombre' es texto, 'Edad' es un número entero y 'Calificación' es un número decimal.

---

### 4. Estadística rápida: `df.describe()`

**¿Qué hace?**
Genera un resumen estadístico para **todas las columnas numéricas**. Es tu mejor amigo para una primera visión general.

**¿Por qué es importante?**
Te da, de un vistazo, la distribución y tendencia central de tus datos numéricos.

**Ejemplo de salida para `df.describe()`:**
```
           Edad    Calificación
count   8.000000       9.000000  # Cuántos valores NO FALTANTES hay
mean   23.125000      85.111111  # El promedio
std     2.031010       9.455815  # Desviación estándar (qué tan dispersos están)
min    21.000000      70.000000  # Valor mínimo
25%    21.750000      78.000000  # Primer cuartil (25% de los datos son <= a este valor)
50%    23.000000      85.000000  # Mediana (el valor de la mitad)
75%    24.250000      92.000000  # Tercer cuartil (75% de los datos son <= a este valor)
max    27.000000      98.000000  # Valor máximo
```

**Interpretación clave:**
- **count vs filas totales:** Si `count` es menor que tus filas totales, ¡tienes valores faltantes!
- **std (Desviación Estándar):** Un número alto significa que los datos están muy dispersos. Uno bajo, que están agrupados cerca de la media.
- **Comparar mean y 50% (mediana):** Si son muy diferentes, sugiere que la distribución está sesgada (hay valores extremos que tiran de la media).

---

### Resumen: El Flujo de Trabajo que Esta Tabla Representa

Cuando recibes un dataset nuevo, este es tu **checklist de supervivencia**:

1.  **`df.dtypes`**: "¿Con qué tipo de datos estoy lidiando?"
2.  **`df.isna().sum()`**: "¿Están mis datos completos? ¿Dónde faltan?"
3.  **`df.duplicated().sum()`**: "¿Tengo datos limpios o hay basura repetida?"
4.  **`df.describe()`**: "¿Cómo se distribuyen mis variables numéricas? ¿Hay valores raros o extremos?"

Al seguir estos pasos, pasas de tener una caja negra (un archivo `.csv` que no conoces) a tener un **mapa claro del terreno** sobre el que vas a construir tu análisis.

¿Te queda claro alguno en particular? ¿Quieres que profundicemos en cómo actuar cuando, por ejemplo, encuentras muchos valores faltantes en una columna?