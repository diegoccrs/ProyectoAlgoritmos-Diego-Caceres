"""
PROYECTO FORMULA 1

Te han contratado para el desarrollo de un nuevo proyecto, un sistema para
la gestión de las carreras de la temporada 2023 de la Fórmula 1. Este sistema
servirá para la venta de entradas, registrar asistencia y más.

El sistema consta de seis (6) módulos fundamentales:
1. Gestión de carreras y equipo
2. Gestión de venta de entradas
3. Gestión de asistencia a las carreras
4. Gestión de restaurantes
5. Gestión de venta de restaurantes
6. Indicadores de gestión (estadísticas)

Nota: Revise la información importante en observaciones

GESTION DE CARRERAS Y EQUIPOS

Este módulo permitirá a los usuarios administrar los equipos y las pistas en
donde ocurrirán las carreras; para eso tendrás que tener en cuenta, que la
información será dada a través de una API, (ver observaciones). Con esta
información deberán desarrollar lo siguiente:

1. Registrar a los constructores con la información proveniente de la API, es
importante que se guarden los siguientes datos:
a. El nombre
b. El id del equipo
c. Su nacionalidad
d. La referencia de sus pilotos (vea el punto 2)

2. Registrar la información de los pilotos proveniente de la API, es importante
que se guarden los siguientes datos:
a. Nombre
b. Apellido
c. Fecha de nacimiento
d. Lugar de nacimiento
e. Número

3. Registrar los carreras con la información proveniente de la API, es importante
que se guarden los siguientes datos:
a. El nombre
b. El número de carrera
c. Fecha de la carrera
d. El circuito en el que se encuentra (ver el punto 4)
e. Podium

4. Registrar los circuitos con la información proveniente de la API, es
importante que se guarden los siguientes datos:
a. El nombre
b. El país
c. La localidad
d. La latitud y longitud

5. Se deberá poder realizar la búsqueda de los carreras en función de los
siguientes filtros:
a. Buscar los constructores por país
b. Buscar los pilotos por constructor
c. Buscar a las carreras por país del circuito
d. Buscar todas las carreras que ocurran en un mes.

6. El administrador de la plataforma deberá ser capaz de finalizar una carrera,
esta operación se encarga de definir un podium de ganadores y asignar a
dichos ganadores una posición (del 1 al 10) para darle los puntos que les
corresponde, si el piloto no están en el top 10, entonces su puntaje es 0. Al
finalizar la temporada al piloto con más puntos se le nombrará campeón
mundial y al constructor con más puntos se le dará el título de campeón de
constructores, los puntos de constructores se calculan sumando los puntajes
de sus pilotos.

a. Puntaje de pilotos
i. 1º clasificado (ganador) 25 puntos
ii. 2º clasificado 18 puntos
iii. 3º clasificado 15 puntos
iv. 4º clasificado 12 puntos
v. 5º clasificado 10 puntos
vi. 6º clasificado 8 puntos
vii. 7º clasificado 6 puntos
viii. 8º clasificado 4 puntos
ix. 9º clasificado 2 puntos
x. 10º clasificado 1 puntos

GESTION DE VENTA DE ENTRADAS

Los organizadores la temporada 2023 de la F1 necesitarán un sistema para
administrar las ventas de sus entradas; para esto necesitará solicitar los siguientes
datos:

1. Datos del cliente:
a. Nombre del cliente
b. Cedula
c. Edad
d. Carrera a la que desea comprar ticket (para esto se deberá mostrar
toda la información de las carreras)
e. Tipo de entrada que desea comprar
i. Si es General: solo podrá ver la carrera en su asiento y su
precio es de $150
ii. Si es VIP; podrá disfrutar del restaurante del circuito, es decir
podrá adquirir productos de dicho restaurante. El precio de una
entrada VIP es de $340

2. Por último le aparecerá el costo de la entrada según los siguientes casos:
a. si su cédula es un número ondulado su entrada tiene un 50% de
descuento y se le notificara al cliente
b. Las entradas hay que sumarle el 16% del impuesto del valor agregado
(IVA)

3. Luego deberá mostrar un mensaje indicando al cliente sus asientos, costo
(con información del subtotal, descuento, IVA y Total) y si desea proceder a
pagar la entrada, de ser así, se ocupa el asiento y se muestra un mensaje de
pago exitoso.

GESTION DE ASISTENCIA DE LAS CARRERAS

En la F1 23, las entradas se compra con anticipación a las carreras, por lo
que es posible que las personas no puedan asistir a la carrera, o que el por el
contrario el circuito esté lleno y se falsifiquen boletos; por tal razón el equipo de
seguridad necesita de un módulo que les permita revisar si los boletos son válidos
para ello deberá:

1. Validar la autenticidad del boleto con un código único del mismo, generado al
momento de comprar el boleto
a. Si el boleto es auténtico deberá modificar la asistencia del carrera

2. Un boleto puede ser considerado falso si el código presentado no coincide
con los códigos del sistema o si el código ya fue utilizado, es decir, un boleto
con ese mismo código ya se usó para entrar al circuito

GESTION DE RESTAURANTES

En los circuitos de la F1 se necesitará un sistema para administrar su
restaurante para sus clientes más importantes (VIP), esto debe tener las siguientes
funcionalidades:

1. Al tener que guardar el producto en su estructura de datos local, luego de
haberla descargado del API, deberá guardar
a. Nombre del alimento/bebida.
b. Clasificación (alimento o bebida).
i. Si es bebida se debe registrar si es alcohólica o no. Si es
alimento se debe guardar si es de empaque o de preparación.
c. Precio (se le deberá sumar el 16% del IVA).

2. Buscar productos por nombre, tipo, o rango de precio.

GESTION DE VENTA DE RESTAURANTES

Para la venta en el restaurante se necesitará que el cliente ya haya comprado
una entrada VIP, esto se validará con su cédula, si es así se procederá de la
siguiente manera:

1. Se guardan los datos del cliente:
a. Cedula.
b. Comida(s) que desee comprar
i. Si la edad el cliente es menor a 18 años no podrá comprar
bebidas alcohólicas

2. Luego deberá mostrarle los productos que desea comprar con el monto total,
siguiendo los siguientes casos:
a. Si la cédula es un número perfecto obtendrá un 15% de descuento.

3. Por último, si el cliente desea proceder con la compra, se le mostrará un
mensaje de pago exitoso con un resumen de su compra donde se muestre el
monto con su subtotal, descuento y total.

4. Se debe restar del inventario la cantidad de productos que el cliente compró

INDICADORES DE GESTION (ESTADISTICAS)

Toda empresa necesita evaluar su gestión y ver que le está funcionando y
que no, para eso es importante un módulo de estadísticas que le indique a los
organizadores de F1 lo siguiente:

1. ¿Cuál es el promedio de gasto de un cliente VIP en una carrera (ticket +
restaurante)?
2. Mostrar tabla con la asistencia a las carreras de mejor a peor, mostrando el
nombre del carrera (nombre de los equipos), estadio en donde se juega,
boletos vendidos, personas que asistieron y la relación asistencia/venta
3. ¿Cuál fue la carrera con mayor asistencia?
4. ¿Cuál fue la carrera con mayor boletos vendidos?
5. Top 3 productos más vendidos en el restaurante.
6. Top 3 de clientes (clientes que más compraron boletos)
7. Realizar gráficos con dichas estadísticas con las librerías de mathplotlib o
Bokeh (Bono).

OBSERVACIONES

● F1 - 2023 posee una API en donde podrás obtener toda su información:
○ Documentación:
https://github.com/Algorimtos-y-Programacion-2223-2/api-proyecto
○ Endpoints:
■ Pilotos:https://raw.githubusercontent.com/Algorimtos-y-Progra
macion-2223-2/api-proyecto/main/drivers.json
■ Constructores:https://raw.githubusercontent.com/Algorimtos-yProgramacion-2223-2/api-proyecto/main/constructors.json
■ Carreras:https://raw.githubusercontent.com/Algorimtos-y-Progra
macion-2223-2/api-proyecto/main/races.json
● La API tiene que funcionar como una opción de pre-cargado de datos antes
de empezar a usar el programa, es decir esta opción crea el estado inicial del
programa, posteriormente no se debe usar la API a menos que se quiera
borrar los datos y cargar su estado inicial
● Se deben usar los conceptos de programación orientado a objetos
● Antes de realizar el código, es imperante que realicen un diagrama de
clases y que la implementación de su proyecto sea uno a uno con el
diagrama
● Se evaluará que el código este comentado (docstring)
● Se evaluará que el sistema contenga validaciones
● Se deberán guardar datos en un archivo TXT para preservar los datos
● El proyecto deberá ser entregado en Github a más tardar el 27 de marzo de
2023 a las 11:59PM

"""