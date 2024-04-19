import streamlit as st
import pandas as pd
import altair as alt

# Data
data = {
    'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Región': ['Global', 'Global', 'Global', 'Global', 'Global', 'Global', 'Global', 'España', 'España', 'España', 'España',  'España', 'España', 'España'],
    'Patrimonio total gestionado (mio €)': [14506.0, 15543.0, 16035.0, 17043.0, 18986.1, 20077.575, 21168.84, 4627.2, 4958.7, 5105.5, 5466.6, 6345.68, 6709.89, 7074.21],
    'Beneficio Neto (mio €)': [49.5, 58.9, 72.5, 71.57, 99.682, 113.098, 124.514, 14.4, 18.7, 23.6, 23.545, 35.832, 47.432, 63.808],
    'Número de empleados': [1377, 1427, 1576, 1561, 1625, 1739, 1827, 439, 455, 503, 498, 514, 555, 583],
    'Clientes': [519670, 532450, 545230, 558010, 570790, 583570, 596350, 165770, 179847, 183923, 188000, 197077, 220153, 223230]
}

df = pd.DataFrame(data)

# Set wide mode by default
st.set_page_config(layout="wide")

# Título de la aplicación
# st.title('Presentación de "En Plan Autónomo"')

# Barra lateral para navegación
st.sidebar.title("# DATA CHASERS")
opcion = st.sidebar.radio("", ('# Home', '# BankValley', '# Data Opportunity', '# Data Governance', '# Data Chasers', '# Nexts steps...'))


# Home
if opcion == '# Home':

    col1, col2, col3 = st.columns([5, 1, 4])  # Ajusta la proporción según necesidad

    with col1:

        st.markdown("""
                    # Bienvenido al portal de 
                    # # DATA CHASERS 
                    #
                    ### Somos  **# Data Chasers**, 
                    ### el nuevo equipo de Analítica Avanzada de BankValley.
                    """)

        st.markdown("""
                    #### Este espacio está dedicado a mostrar cómo la integración de nuevas herramientas analíticas y el aprovechamiento estratégico del dato están creando oportunidades de negocio únicas.
                    """)

        st.markdown('#')

        st.markdown("""
                ### ¿Qué encontrarás aquí?
                - **# BankValley**: Explora quiénes somos y por qué somos un referente en banca ética, sostenible e innovadora.
                - **# Data Oportunity**: En Plan Autónomo. Descubre nuestra primera propuesta de oportunidad de negocio. Un ejemplo concreto de lo que podemos lograr con el poder del análisis de datos.
                - **# Data Chasers**: Conoce más sobre nuestra filosofía y el equipo detrás de la innovación.
                - **# Data Culture**: Aprende sobre la cultura de datos que estamos promoviendo dentro de la empresa, diseñada para potenciar cada decisión con base en análisis rigurosos y datos fiables.

                #      
                ### Únete a nosotros para transformar el futuro de BankValley 
                ### a través del dato!!
                """)
    with col2:
        st.markdown('#')

    with col3:
        st.image("imgs/BankValley_1.jpeg", caption="BankValley Madrid", width=450)

# BanValley
elif opcion == '# BankValley':

    st.markdown("""
                # BankValley
                ### Referente en Banca Ética y Sostenible
                #### Descubre cómo nuestra misión, valores y acciones están transformando la industria financiera hacia un futuro más responsable y sostenible.
                """)


    col1, col2 = st.columns([1, 1])  # Ajusta la proporción según necesidad

    with col1:


        with st.expander("#### Filosofía y Valores"):
            st.write("""
                    - **Líder en Banca Ética y Sostenible**  
                    En BankValley, estamos comprometidos con el cambio social, ambiental y cultural, integrando la sostenibilidad en el núcleo de nuestra estrategia financiera. Nos esforzamos por ser agentes de cambio, liderando el camino hacia una industria bancaria más consciente y respetuosa del entorno.
                    
                    - **Enfoque Sostenible**  
                    Nuestra misión va más allá del negocio tradicional; rechazamos activamente los fondos y las inversiones que no cumplen con nuestros estrictos criterios de sostenibilidad. Esta postura nos permite mantener un compromiso firme con el desarrollo sostenible, influenciando positivamente las prácticas financieras en el mercado.
                    
                    - **Agentes de Cambio**  
                    Como pioneros en incorporar la responsabilidad social y ambiental en todas nuestras operaciones, estamos estableciendo nuevos estándares en el sector bancario. Nuestro enfoque progresista no solo responde a la demanda actual de mayor transparencia y ética en las finanzas, sino que también modela el impacto que una empresa puede tener en la sociedad.
                    """)

        with st.expander("#### Inversiones Sostenibles"):
            st.write("""
                    - **Compromiso con el Futuro**   
                    Nuestro portafolio de inversiones refleja nuestro compromiso con un futuro sostenible. Nos centramos en sectores como la agricultura ecológica, la bioconstrucción, el transporte eficiente y las energías limpias.
                    
                    - **Impacto Medioambiental**   
                    Ofrecemos fondos de inversión y ecodepósitos que buscan no solo un retorno financiero, sino también un impacto medioambiental positivo, reafirmando nuestro compromiso con la sostenibilidad a largo plazo.
                    """)

    with col2:
        with st.expander("#### Clientes y Enfoque de Negocio"):
            st.write("""
                    - **Clientes Conscientes**   
                    Dirigimos nuestros servicios a clientes que valoran la ética y la responsabilidad ecológica en sus decisiones económicas. Nuestra base de clientes incluye tanto individuos como empresas que están alineadas con valores progresistas.
                                        
                    - **Apoyo a Autónomos y PYMEs**  
                    Más del **21% de nuestros clientes son autónomos**, superando la media nacional, con un fuerte compromiso en el apoyo a pequeñas y medianas empresas.
                    
                    - **Apoyo a Proyectos Sostenibles**   
                    Hasta la fecha, hemos apoyado más de 4,000 proyectos que comparten nuestra visión de un modelo económico alternativo y sostenible.
                    """)

        with st.expander("#### Hitos de BankValley"):

            # Creación del gráfico de scatter plot
            chart = alt.Chart(df).mark_circle().encode(
                x=alt.X('Año:O', axis=alt.Axis(labelAngle=-45)),
                y=alt.Y('Beneficio Neto (mio €)', title='Beneficio Neto (mio €)'),
                size=alt.Size('Clientes', title='Clientes (K)', scale=alt.Scale(range=[100, 1000])),
                color='Región',
                tooltip=['Año', 'Beneficio Neto (mio €)', 'Clientes', 'Región']
            ).properties(
                width=600,
                height=400,
                title='Comparativa del Beneficio Neto y Clientes entre Global y España'
            )

            # Mostrar gráfico en Streamlit
            st.altair_chart(chart, use_container_width=True)

            st.markdown("""
                        - **Crecimiento Sostenido**  
                        Desde nuestra llegada a España en 2004, hemos crecido notablemente, gestionando un patrimonio que ha escalado a más de €6,431 millones en 2023.
                        
                        - **Expansión de la Base de Clientes**  
                        Nuestro número de clientes ha aumentado significativamente, de 149K en 2013 a 190K en 2023, reflejando una confianza creciente en nuestro modelo de banca ética.
                        
                        - **Aumento en la Plantilla**  
                        Nuestros empleados han crecido proporcionalmente, de 291 en 2013 a 583 en 2023, demostrando el éxito y la expansión del banco.
                        """
                        )

    st.image("imgs/BankValley_2.jpeg", caption="Oficinas de BankValley Madrid")

# Data opportunitty
elif opcion == '# Data Opportunity':

    st.image("imgs/BankValley_4.jpeg", caption="En Plan autónomo")
    
    st.markdown("""
                ### Data Opportunity  
                # 'En Plan Autónomo'
                ###
                **'En Plan Autónomo'** aprovecha la tecnología, las personas y la cultura del dato para ofrecer soluciones financieras personalizadas.

                Desbloqueamos nuevas posibilidades para autónomos, fusionando tecnología de vanguardia y financiación ética para convertir la viabilidad 
                económica en una realidad sostenible.  
                 
                Este enfoque fomenta un cambio positivo en la forma en que el banco se relaciona con el segmento de los autónomos, alineando nuestras operaciones 
                no solo con nuestras metas económicas, sino también con nuestros valores éticos y de sostenibilidad.
                """)
    

    col1, col2 = st.columns([1, 1])  

    with col1:
        with st.expander("#### La situación actual"):
            st.write("""
                    - **Dificultades para Autónomos**:   
                    Los autónomos enfrentan barreras significativas al solicitar hipotecas debido a los estrictos requisitos de garantía y una percepción 
                    general de alto riesgo. Esta situación limita su acceso a financiación necesaria para sus negocios y proyectos personales.  
                    
                    - **Evaluación de Riesgo Inadecuada**:  
                    Las herramientas estándar de evaluación de riesgo no capturan adecuadamente la realidad financiera de los autónomos, lo que resulta en 
                    oportunidades perdidas tanto para el banco como para sus clientes, potencialmente desestimando clientes solventes.  

                    - **Falta de Personalización**:  
                    El mercado actual carece de enfoques personalizados en la evaluación de solicitudes de hipoteca para autónomos, ignorando las particularidades
                    de su flujo de ingresos y estabilidad financiera.  
                    
                    - **Clientes Alineados con la Misión del Banco**:  
                    Una proporción significativa de clientes autónomos de BankValley está involucrada en proyectos sostenibles y éticos, lo que refleja los valores 
                    y la misión del banco, destacando la necesidad de ofrecer productos que se alineen con sus principios.
                    """)
    with col2:
        with st.expander("#### Soluciones alternativas y sus limitaciones"):
            st.write("""
                    - **Pago al Contado**:  
                    Esta opción, aunque ideal, no es viable para la mayoría de los autónomos debido a los altos requerimientos de capital inicial, 
                    lo que limita severamente su accesibilidad a propiedades.  

                    - **Hipotecas de Corto Plazo**:  
                    Las hipotecas con términos de hasta 10 años, aunque disponibles, resultan en pagos mensuales elevados que no son sostenibles para 
                    autónomos con ingresos variables.  

                    - **Entidades Financieras de Menor Reputación**:  
                    Frente a la rigidez de bancos tradicionales, los autónomos pueden verse forzados a optar por entidades con menos credibilidad, que 
                    pueden ofrecer condiciones menos favorables y más riesgosas.  

                    - **Préstamos Federados y Cuentas Pignoradas**:  
                    Estas opciones de financiación, aunque creativas, requieren que los autónomos bloqueen una cantidad significativa de dinero como garantía, 
                    restringiendo su liquidez y flexibilidad financiera.
                    """)

    with st.expander("#### Nuestra propuesta"):
        st.write("""
                 ## 'En Plan Autónomo'
                 #
                - **Evaluación de Riesgo Personalizada**:  
                Utilizando técnicas avanzadas de aprendizaje automático, 'En Plan Autónomo' analiza patrones financieros detallados para ofrecer créditos preaprobados. Este enfoque permite ajustar los límites de crédito individualmente, ofreciendo préstamos que varían desde 40.000€ hasta 3 millones de euros, adaptándose a las necesidades y capacidades financieras específicas de cada autónomo, desde pequeños emprendedores hasta grandes empresarios.

                - **Integración de Productos y Servicios**:  
                Este plan no solo proporciona hipotecas, sino que también integra seguros y beneficios fiscales personalizados que reflejan las necesidades individuales y la situación laboral del autónomo. Considera variables como el impacto fiscal de la actividad empresarial y la generación de empleo, ofreciendo así una solución financiera integral que va más allá de la simple concesión de crédito.

                - **Blockchain para Inversión Colaborativa**:  
                'En Plan Autónomo' implementa la tecnología blockchain para crear un sistema de financiación colectiva transparente y seguro. Esto permite que otros clientes del banco participen como inversores en hipotecas de proyectos alineados con los valores de sostenibilidad y responsabilidad ética de BankValley. Cada transacción y acuerdo se registra de manera indelible, garantizando confianza y claridad para todos los involucrados.

                - **Flexibilidad de Pago**:  
                Reconociendo la naturaleza fluctuante de los ingresos de muchos autónomos, este plan ofrece flexibilidad en los términos de pago. Los sistemas de scoring y predicción basados en big data permiten ajustar periódicamente las condiciones del préstamo en respuesta a los cambios en la situación financiera del cliente, lo que puede incluir la reducción de las cuotas en períodos de menores ingresos o la reestructuración del plan de pago según las proyecciones de crecimiento del negocio.

                - **Acceso Simplificado**:  
                El proceso de solicitud y gestión de 'En Plan Autónomo' es completamente digital, eliminando la necesidad de trámites burocráticos y visitas a sucursales. Los autónomos pueden acceder a todos los servicios a través de una plataforma intuitiva que incluye soporte virtual, facilitando una experiencia de usuario fluida y eficiente. Este enfoque no solo mejora la accesibilidad y la comodidad para el usuario, sino que también agiliza el proceso de aprobación y desembolso del crédito.
                """)
    
    with st.expander("#### Estrategia del dato y Sinergias internas"):

        col1, col2 = st.columns([1, 1])  

        with col1:
            st.write("""
                    #### Tecnología:                    
                    - **Plataforma de Análisis en Cloud**:  
                     En los últimos años, Bankvalley ha ido desplegando su infraestructura en la nube, desarrollando sistemas que procesan grandes volúmenes de datos financieros.  
                     Esta capacidad nos permite realizar evaluaciones del riesgo crediticio de manera mucho más precisa y ágil, sin la necesidad de infracestructura adicional.

                     - **Integración de Herramientas Avanzadas**:   
                     Utilizamos la infraestructura tecnológica ya existente del banco, incorporamos soluciones de Anallítica Avanzadas, aprendizaje automático e IA.  
                     Esta integración mejora significativamente la toma de decisiones y abre nuevas oportunidades de negocio al permitir un análisis más profundo y 
                     preciso de los datos financieros.

                    #### Personas y Cultura:
                    - **Equipo Interdisciplinario**:  
                     Hemos formado un nuevo departamento especializado en análisis de datos y algoritmos de inteligencia artificial.  
                     Este equipo trabaja en estrecha colaboración con otros departamentos para asegurar que las soluciones de datos se integren de manera efectiva 
                     en todas las áreas del banco.
                    
                    - **Fomento de la Cultura del Dato**:  
                     Iniciamos diversas iniciativas para educar y promover la comprensión y el uso estratégico de los datos entre todos los empleados del banco.  
                     Estas actividades están diseñadas para transformar la cultura organizacional y hacer que el pensamiento basado en datos sea una parte central 
                     de nuestra identidad corporativa.

                    """)
            
            with col2:
                st.write("""
                    #### Datos:
                    - **Acceso y Mejora de Datos**:  
                        Aprovechamos los datos de clientes existentes y los complementamos con datos externos para enriquecer el perfilado y la segmentación de nuestros clientes.  
                         Esta estrategia nos permite no solo mejorar la precisión de nuestro scoring, sino también ofrecer productos más personalizados.
                    
                    - **Privacidad y Ética de Datos**:  
                        Nos comprometemos a garantizar la protección de la privacidad de nuestros clientes, a asegurar un uso ético de los datos en todos nuestros procesos y
                         a prevenir activamente el sesgo en nuestros modelos.  
                         La integridad y seguridad de los datos son fundamentales para mantener la confianza de nuestros clientes.

                    #### Algoritmos:
                    - **Algoritmos de Machine Learning**:  
                        Empleamos modelos predictivos y de clusterización, siendo posible considerar y ponderar decenas de variables para llevar a otro nivel nuestro scoring de riesgo crediticio.  
                         Estos modelos están diseñados para considerar no solo la estabilidad financiera de los autónomos sino también su potencial de crecimiento, ofreciendo así una evaluación más justa y beneficiosa para ambos, el cliente y el banco.
                    
                    - **Personalización y Adaptabilidad**:  
                        Utilizamos algoritmos para personalizar productos financieros y adaptar las condiciones de las hipotecas a las necesidades individuales y al comportamiento financiero de cada autónomo, permitiendo una flexibilidad que refleja la realidad económica de nuestros clientes.

                    """)

        
    with st.expander("#### KPIs para medir el Éxito"):

        col1, col2 = st.columns([1, 1])  

        with col1:
            st.write("""
                    - **Tasa de Adopción del Producto**:  
                    Medición del porcentaje de autónomos a los que se les ha ofrecido 'En Plan Autónomo' respecto al total de clientes autónomos del banco.  
                    
                    - **Tasa de Conversión**:  
                    Porcentaje de autónomos que efectivamente contratan tras la oferta.  
                    
                    - **Rendimiento Financiero**:  
                    Evaluación del beneficio neto de las hipotecas concedidas bajo 'En Plan Autónomo' y comparación con la tasa de interés media de otros productos 
                    hipotecarios del banco.  
                    
                    - **Calidad del Crédito**:  
                    Monitoreo del porcentaje de impagos o morosidad en 'En Plan Autónomo' en comparación con productos estándar del banco y observación de cambios en 
                    la puntuación crediticia media de los clientes autónomos tras la implementación del producto.  
                    
                    - **Impacto en la Sostenibilidad y la Misión del Banco**:  
                    Número o porcentaje de proyectos financiados a través de 'En Plan Autónomo' que están alineados con los objetivos de sostenibilidad y ética de BankValley.  
                    
                    - **Satisfacción del Cliente**:  
                    Resultados de encuestas de satisfacción específicas y número de referencias o recomendaciones del producto por parte de clientes 
                    autónomos existentes.  
                    """)
            
        with col2:
            st.image("imgs/img1.jpg", caption="BankValley Madrid", width = 550)


    # with st.expander("#### Business Case"):


# Data Governance
elif opcion == '# Data Governance':

    col1, col2 = st.columns([3, 2])  

    with col1:
        st.markdown("""
                    # Data Governance

                    #### Una política del dato bien definida aporta a BankValley un marco robusto para tomar decisiones estratégicas informadas, potenciando la eficiencia operativa y la competitividad en el mercado.
                    
                    La implementación efectiva de una estrategia de gobernanza de datos es esencial para organizaciones como BankValley, 
                    donde la ética y la responsabilidad son pilares fundamentales. Al asegurar una gestión de datos adecuada, no solo se optimizan las operaciones internas, 
                    sino que también se refuerza la confianza en nuestra institución financiera. Investigaciones indican que una mala gobernanza de datos puede llevar al 
                    fracaso de hasta un 40% de los proyectos empresariales, lo cual subraya la necesidad de establecer prácticas robustas de manejo de datos desde el inicio.

                    Esta propuesta ayudará a BankValley a enfrentar los desafíos de transformarse en una organización completamente orientada a datos, 
                    asegurando que la calidad y la integridad de los datos se mantengan en cada paso del camino.
                    """)
        
    with col2:
        st.image("imgs/BankValley_5.jpeg", caption="Hacia un Data Governance")


    with st.expander("#### Organización Existente y Normas Culturales"):
        col1, col2, col3 = st.columns([1, 1, 1])  

        with col1:
            st.write("""
                    #### Cultura:
                     
                    - **Decisión Basada en Datos:**  
                     Proponemos fortalecer la cultura donde las decisiones se toman basadas en datos rigurosos, asegurando que líderes y main players estén entrenados en 
                     interpretación de datos.
                    
                     - **Comités de Datos:**  
                     Implementar comités multidisciplinares que incluyan expertos en datos para asegurar que las decisiones estén bien fundamentadas y respaldadas por 
                     análisis completos.
                    """)

        with col2:
            st.write("""
                    #### Modelo Operativo:
                     
                    - **Adopción de un Modelo Federado:**  
                     Proponemos una transición gradual hacia un modelo operativo federado que permita avanzar hacia la democratización del dato en todas las áreas de manera gradual.
                    
                     - **Implementación Uniforme de Políticas:**  
                     Asegurar que las políticas de datos y las mejores prácticas se apliquen de manera uniforme en todas las áreas de negocio. 
                     Nos comprometemos a prestar todo el apoyo a las diferentes áreas para asegurar una transición fluida.
                    """)

        with col3:
            st.write("""
                    #### Roles:
                     
                    - **CDO (Chief Data Officer):**  
                     Este rol será clave en supervisar la visión y estrategia de datos del banco, asegurando el alineamiento con los objetivos estratégicos globales y 
                     promoviendo la cultura de datos en BankValley.
                    
                     - **Data Owners y Data Stewards:**  
                     Serán los custodios de la calidad de los datos, trabajando para mantener la integridad y cumplimiento a lo largo del ciclo de vida de los datos.
                     
                     - **Data Scientists y Analysts:**  
                     Fundamental para el desarrollo de modelos y análisis que descubren nuevas oportunidades basadas en insights de datos. 
                     Forma parte de la estrategia que se integren gradualmente en todas las áreas de negocio para impulsando las decisiones basadas en datos.
                    """)

    with st.expander("#### Habilitadores Tecnológicos"):
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.write("""
                    #### Glosario de Negocio:
                     
                    - **Establecimiento de un Lenguaje Común:**  
                    Propuesta para crear un glosario empresarial que defina claramente todos los términos clave, KPIs y métricas, facilitando un lenguaje unificado y 
                    evitando malentendidos en la interpretación de los datos.
                     
                    - **Actualización y Mantenimiento Continuo:**  
                    Asegurar que el glosario se mantenga actualizado con las últimos cambios de negocio, garantizando que todos los empleados tengan acceso a la 
                     misma información y la interpretación se unívoca.
                    """)

        with col2:
            st.write("""
                    #### Gestión de la Calidad del Dato:
                     
                    - **Definición de Estándares de Calidad:**  
                    Establecer un marco riguroso que defina las dimensiones de la calidad de los datos como la precisión, actualidad, relevancia, consistencia o la fiabilidad,  
                    asegurando que los datos que respaldan nuestras decisiones y operaciones sean de calidad.
                     
                    - **Monitorización y Reporte Continuo:**  
                    Implementar herramientas y procesos para monitorizar continuamente la calidad de los datos y reportar cualquier desviación de los estándares establecidos, 
                     permitiendo intervenir rápidamente.
                    """)

        with col3:
            st.write("""
                    #### Plan de Comunicación:
                     
                    - **Implementación de un Plan de Comunicación:**  
                    Desarrollar un plan de comunicación que incluya regularmente la formación cultura y gobierno del dato para todos los empleados, 
                     apostando por su compromiso y comprensión de la importancia de este cambio.
                     
                    - **Feedback y Adaptación:**  
                    Establecer canales de feedback que permitan a los empleados expresar sus inquietudes y sugerencias respecto a esta transición, 
                     asegurando que el plan de comunicación se adapte y evolucione según las necesidades del personal.
                    """)

# Data Chasers
elif opcion == '# Data Chasers':

    st.image("imgs/BankValley_6.jpeg", caption="Cthulhu llamando a la revolución del Dato")

    st.markdown("""
                # # Data Chasers
                ### Guiados por Cthulhu, exploramos las profundidades de los datos e invocamos poderosos insights:
                """)

    st.markdown("""
                ##### Fomentar un cambio cultural en BankValley es esencial para hacer que los datos sean democráticos, accesibles, valiosos y accionables. 
                ##### Al hacerlo, mejoramos la toma de decisiones y promovemos un entorno donde la innovación y la ética impulsan nuestra visión.
                """)
    
    
    col1, col2, col3 = st.columns(3)
        
    with col1:
        with st.expander("#### Cthulhu: Mascota y Embajador"):
            st.write("""
                     - **Alineación con Análisis Avanzado**:  
                    Como una criatura de misterios ocultos y sabiduría arcaica, Cthulhu simboliza perfectamente la exploración y el descubrimiento profundo que caracterizan la analítica avanzada. Su figura mitológica despierta curiosidad y representa la constante búsqueda de conocimiento, haciéndolo el emblema ideal para un equipo que busca desentrañar los secretos ocultos en los datos.
                    
                    - **Figura Inspiradora**:  
                    Cthulhu no solo inspira nuestro enfoque sino que también personifica la cultura de datos de BankValley, 
                    facilitando la aceptación y el entusiasmo por parte de todos los empleados.
                    
                    - **Icono Cultural**:  
                    Cthulhu es clave en nuestras comunicaciones internas, ayudando a hacer tangible el impacto de los datos en nuestro banco.                    
                    """)
        
    with col2:
        with st.expander("#### Invocando al Dato"):
            st.write("""
                    - **El Rincón de Cthulhu**:  
                    Espacio de aprendizaje y asistencia para quienes se inician en el uso de datos, haciendo que la analítica sea más accesible.
                    
                    - **Encantamientos Arcanos**:  
                    Talleres prácticos que muestran el análisis de datos en acción para tomar decisiones de negocio comprensibles y aplicables, 
                    impulsando con ejemplos prácticos la alfabetización de datos.
                    
                    - **'Cthulhu’s Code Crypt'**:  
                    Cursos intensivos y muy prácticos en herramientas y lenguajes de programación para análisis de datos, diseñados para mejorar las habilidades técnicas de los empleados.
                    """)

    with col3:
        with st.expander("#### Medir el Progreso"):
            st.write("""
                    - **Adopción de Herramientas Analíticas**:  
                    Seguimiento del incremento en el uso de herramientas analíticas entre los empleados para garantizar una cultura de datos efectiva.
                    
                    - **Calidad en la Toma de Decisiones**:  
                    Evaluamos cómo la implementación de data products y decisiones basadas en análisis están transformando las operaciones en el banco.
                    
                    - **Engagement**:  
                    Medimos la participación y satisfacción en eventos y talleres de datos, seguimiento del NPS para asegurar la efectividad de nuestras iniciativas y fomentar una mejora continua.
                    """)

# Nexts Steps...
elif opcion == '# Nexts steps...':
    st.write("""
                #### Lecciones Aprendidas:
             
                - La adopción efectiva de estrategias basadas en datos requiere un compromiso organizacional profundo y una cultura que valore y entienda 
                el uso de datos como una herramienta estratégica.

                - La educación continua y el desarrollo de habilidades en análisis de datos son fundamentales para capacitar a todos los niveles de la organización, 
                asegurando que las decisiones se tomen sobre bases sólidas y bien informadas.

                - La transparencia en la gestión y uso de los datos es crucial para mantener la confianza tanto interna como externa en las iniciativas de datos.

                #### Factores Clave:
             
                - El apoyo continuo de la alta dirección y la integración de los análisis de datos en la toma de decisiones estratégicas son esenciales para el 
                éxito a largo plazo del proyecto.

                - La colaboración entre departamentos y la clara definición de roles y responsabilidades en la gestión de datos garantizan la coherencia y eficiencia 
                de las iniciativas basadas en datos.

                - Fomentar una actitud de aprendizaje y mejora continua entre todos los empleados para adaptarse a las cambiantes tecnologías y prácticas del mercado.

                #### Posibles Stoppers:
             
                - Un fracaso potencial podría deberse a la resistencia al cambio dentro de la organización o a deficiencias en la infraestructura tecnológica, 
                lo que limitaría la capacidad de aprovechar plenamente el análisis de datos.

                - La falta de alineación entre los objetivos del proyecto de datos y los objetivos estratégicos del banco podría resultar en iniciativas que no cuentan 
                con el respaldo necesario o que no cumplen con las expectativas establecidas.

                - La subestimación de los recursos necesarios para la formación y el desarrollo de capacidades en el uso de datos puede resultar en una implementación
                incompleta y beneficios no realizados.

                #### Próximos Pasos: Implementación de IA Generativa y Análisis Avanzado
                
                - **Corto Plazo**: Implementación de IA generativa para interacción directa y soporte al cliente, mejorando la personalización y la eficiencia del 
                servicio al cliente mediante chatbots avanzados que pueden generar respuestas contextuales en tiempo real.
                
                - **Medio Plazo**: Utilización de IA basadas en modelos de Mixture of Experts (MoE) para la generación de insights profundos y la automatización de 
             la toma de decisiones en tiempo real. Estos modelos permitirán a BankValley responder dinámicamente a las condiciones del mercado y ajustar las estrategias 
             de inversión y gestión de riesgos de manera más efectiva.
                
                - **Largo Plazo**: Exploración de aplicaciones de computación cuántica en el sector bancario para resolver problemas complejos y optimizar operaciones 
             a una escala previamente inalcanzable. Esto incluirá desde la optimización de carteras hasta la mejora de los modelos de criptografía y seguridad.
                """)
