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
opcion = st.sidebar.radio("", ('# Home', '# BankValley', '# Data Opportunity', '# Data Team', '# Data Culture', '# Nexts steps...'))


# Home
if opcion == '# Home':

    st.markdown("""
                # Bienvenido a # DATA CHASERS

                ### ¡Hola! 
                ### Somos  **# Data Chasers**, el equipo de Analítica Avanzada de BankValley.

                #### Este espacio está dedicado a demostrar cómo la integración de nuevas herramientas analíticas y el aprovechamiento estratégico del dato están creando oportunidades de negocio únicas.
                """)

    st.markdown('#')
    st.markdown('#')

    col1, col2 = st.columns([6, 4])  # Ajusta la proporción según necesidad

    with col1:
        st.markdown("""
                ### ¿Qué encontrarás aquí?
                - **# BankValley**: Explora quiénes somos y por qué somos un referente en banca ética, sostenible e innovadora.
                - **# Data Oportunity**: En Plan Autónomo. Descubre nuestra primera propuesta de oportunidad de negocio. Un ejemplo concreto de lo que podemos lograr con el poder del análisis de datos.
                - **# Data Chasers**: Conoce más sobre nuestra filosofía y el equipo detrás de la innovación.
                - **# Data Culture**: Aprende sobre la cultura de datos que estamos promoviendo dentro de la empresa, diseñada para potenciar cada decisión con base en análisis rigurosos y datos fiables.

                Únete a nosotros para transformar el futuro de BankValley a través del dato.
                """)
        
    with col2:
        st.image("imgs\img1.jpg", caption="Imagen representativa de BankValley", width=450)

# BanValley
elif opcion == '# BankValley':
    st.markdown("""
                # BankValley
                ### Referente en Banca Ética y Sostenible
                Descubre cómo nuestra misión, valores y acciones están transformando la industria financiera hacia un futuro más responsable y sostenible.
                """)

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

    with st.expander("#### Clientes y Enfoque de Negocio"):
        st.write("""
                 - **Clientes Conscientes**   
                 Dirigimos nuestros servicios a clientes que valoran la ética y la responsabilidad ecológica en sus decisiones económicas. Nuestra base de clientes incluye tanto individuos como empresas que están alineadas con valores progresistas.
                 
                 - **Apoyo a Proyectos Sostenibles**   
                 Hasta la fecha, hemos apoyado más de 4,000 proyectos que comparten nuestra visión de un modelo económico alternativo y sostenible.
                 """)

    with st.expander("#### Hitos de BankValley"):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
                        - **Crecimiento Sostenido**  
                        Desde nuestra llegada a España en 2004, hemos crecido notablemente, gestionando un patrimonio que ha escalado a más de €6,431 millones en 2023.
                        
                        - **Expansión de la Base de Clientes**  
                        Nuestro número de clientes ha aumentado significativamente, de 149K en 2013 a 190K en 2023, reflejando una confianza creciente en nuestro modelo de banca ética.
                        
                        - **Aumento en la Plantilla**  
                        Nuestros empleados han crecido proporcionalmente, de 291 en 2013 a 583 en 2023, demostrando el éxito y la expansión del banco.
                        
                        - **Apoyo a Autónomos y PYMEs**  
                        Más del 21% de nuestros clientes son autónomos, superando la media nacional, con un fuerte compromiso en el apoyo a pequeñas y medianas empresas.
                        """)

        with col2:
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

# Data opportunitty
elif opcion == '# Data Opportunity':

    st.markdown("""
                # Data Opportunity
                ## "En Plan Autónomo"
                ### Propuesta Única de Valor
                "En Plan Autónomo" desbloquea nuevas posibilidades para autónomos, fusionando tecnología de vanguardia y financiación ética para
                 convertir la viabilidad económica en una realidad sostenible.
                """)

    with st.expander("#### Problema"):
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

    with st.expander("#### Alternativas y sus Limitaciones"):
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

    with st.expander("#### Soluciones Candidatas"):
        st.write("""
                - **Scoring Personalizado para Preconcesión**:  
                 Implementación de un modelo de scoring avanzado, utilizando datos de transacciones y comportamiento financiero, para ofrecer hipotecas preconcedidas 
                 a autónomos, adaptándose mejor a sus necesidades y capacidad de pago.  
                
                - **Paquetización de Productos con Incentivos**:  
                 Diseño de ofertas personalizadas que integren hipotecas con seguros profesionales y de vida, ofreciendo beneficios mutuos que incluyan descuentos o 
                 condiciones favorables en los intereses.  
                
                - **Financiación Colaborativa con Blockchain**:  
                 Utilización de blockchain para crear un sistema de financiación colectiva que permita a otros clientes del banco invertir en hipotecas de proyectos 
                 alineados con los valores de BankValley, asegurando transparencia y seguridad.  
                
                - **Asesoría Financiera Integral para Autónomos**:  
                 Proporcionar un servicio de asesoría especializado que combine la evaluación de hipotecas con asesoramiento financiero estratégico, ayudando a los 
                 autónomos a optimizar su salud financiera a largo plazo.  
                
                - **Flexibilidad en Garantías y Términos de Pago**:  
                 Introducir condiciones de hipoteca con garantías más flexibles y plazos de amortización adaptados al flujo de ingresos variable de muchos autónomos, 
                 permitiendo pagos más bajos durante periodos de menor ingreso.  
                """)

    with st.expander("#### En Plan Autónomo"):
        st.write("""
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
    
    with st.expander("#### Sinergias internas"):
        st.write("""
                **Tecnología:**
                - **Integración de Herramientas Avanzadas**: Utilizamos la infraestructura tecnológica existente del banco, enriqueciéndola con soluciones avanzadas de inteligencia artificial y aprendizaje automático. Esta integración mejora significativamente la toma de decisiones y abre nuevas oportunidades de negocio al permitir un análisis más profundo y preciso de los datos financieros.
                - **Plataforma de Análisis de Big Data**: Hemos desarrollado sistemas que procesan grandes volúmenes de datos financieros en tiempo real. Esta capacidad nos permite realizar evaluaciones del riesgo crediticio de manera mucho más precisa y ágil, adaptándonos a las necesidades dinámicas del mercado y de nuestros clientes.

                **Personas / Cultura:**
                - **Equipo Interdisciplinario**: Hemos formado un nuevo departamento especializado en análisis de datos y algoritmos de inteligencia artificial. Este equipo trabaja en estrecha colaboración con otros departamentos para asegurar que las soluciones de datos se integren de manera efectiva en todas las áreas del banco.
                - **Fomento de la Cultura del Dato**: Iniciamos diversas iniciativas para educar y promover la comprensión y el uso estratégico de los datos entre todos los empleados del banco. Estas actividades están diseñadas para transformar la cultura organizacional y hacer que el pensamiento basado en datos sea una parte central de nuestra identidad corporativa.

                **Datos:**
                - **Acceso y Mejora de Datos**: Aprovechamos los datos de clientes existentes y los complementamos con datos externos para enriquecer los perfiles de riesgo. Esta estrategia nos permite no solo mejorar la precisión de nuestro scoring, sino también ofrecer productos más personalizados.
                - **Privacidad y Ética de Datos**: Nos comprometemos a garantizar la protección de la privacidad de nuestros clientes y a asegurar un uso ético de los datos en todos nuestros procesos. La integridad y seguridad de los datos son fundamentales para mantener la confianza de nuestros clientes.

                **Algoritmos:**
                - **Algoritmos de Machine Learning**: Empleamos modelos predictivos como Random Forest o Gradient Boosting para el scoring crediticio. Estos modelos están diseñados para considerar no solo la estabilidad financiera de los autónomos sino también su potencial de crecimiento, ofreciendo así una evaluación más justa y beneficiosa para ambos, el cliente y el banco.
                - **Personalización y Adaptabilidad**: Utilizamos algoritmos para personalizar productos financieros y adaptar las condiciones de las hipotecas a las necesidades individuales y al comportamiento financiero de cada autónomo, permitiendo una flexibilidad que refleja la realidad económica de nuestros clientes.

                **"En Plan Autónomo" como Concepto Integral:** aprovecha la tecnología, las personas y la cultura del dato para ofrecer soluciones financieras personalizadas. Este enfoque fomenta un cambio positivo en la forma en que el banco se relaciona con el segmento de los autónomos, alineando nuestras operaciones no solo con nuestras metas económicas, sino también con nuestros valores éticos y de sostenibilidad.
                """)

    with st.expander("#### KPIs para medir el Éxito"):
        st.write("""
                - **Tasa de Adopción del Producto**:  
                 Medición del porcentaje de autónomos a los que se les ha ofrecido 'En Plan Autónomo' respecto al total de clientes autónomos del banco.  
                
                - **Tasa de Conversión**:  
                 Porcentaje de autónomos que efectivamente contratan 'En Plan Autónomo' tras la oferta.  
                
                - **Rendimiento Financiero**:  
                 Evaluación del beneficio neto de las hipotecas concedidas bajo 'En Plan Autónomo' y comparación con la tasa de interés media de otros productos 
                 hipotecarios del banco.  
                
                - **Calidad del Crédito**:  
                 Monitoreo del porcentaje de impagos o morosidad en 'En Plan Autónomo' en comparación con productos estándar del banco y observación de cambios en 
                 la puntuación crediticia media de los clientes autónomos tras la implementación del producto.  
                
                - **Impacto en la Sostenibilidad y la Misión del Banco**:  
                 Número o porcentaje de proyectos financiados a través de 'En Plan Autónomo' que están alineados con los objetivos de sostenibilidad y ética de BankValley.  
                
                - **Satisfacción del Cliente**:  
                 Resultados de encuestas de satisfacción específicas para 'En Plan Autónomo' y número de referencias o recomendaciones del producto por parte de clientes 
                 autónomos existentes.  
                """)

    # Ejemplo de gráfico
    # Datos genéricos creados para el ejemplo
    data = {
        'Año': [2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Clientes Autónomos': [500, 600, 700, 800, 900, 1000, 1100],
        'Hipotecas Concedidas': [20, 25, 30, 35, 40, 45, 50]
    }

    # Creación del DataFrame
    df = pd.DataFrame(data)

    # Código para visualizar un gráfico en Streamlit usando Altair
    chart = alt.Chart(df).mark_line(point=True).encode(
        x='Año:N',
        y=alt.Y('Clientes Autónomos', axis=alt.Axis(title='Número de Autónomos')),
        color=alt.Color('Hipotecas Concedidas', legend=alt.Legend(title="Hipotecas Concedidas por Año"))
    ).properties(
        title='Evolución de Autónomos y Hipotecas Concedidas'
    )

    # Usar Streamlit para mostrar el gráfico
    st.altair_chart(chart, use_container_width=True)

# Data Team
elif opcion == '# Data Team':
    st.markdown("""
                # Data Strategy
                ### Visión y Equipo
                #### Liderar la transformación de BankValley en innovación financiera y crecimiento sostenible a través de la analítica avanzada.
                - **Equipo:** Expansión del equipo actual con expertos en riesgo, ingeniería de datos y ciencia de datos para fortalecer la propuesta de valor.
                - **Conocimiento:** Necesidad de formación especializada en Big Data, Machine Learning, negocio bancario y regulaciones de datos.
                - **Stakeholders:** Colaboración estrecha con áreas internas del banco, reguladores y seguimiento de la competencia para mantener la ventaja competitiva.
                - **Infraestructura:** Utilización de la infraestructura en la nube existente del banco para el análisis y desarrollo ágil del nuevo producto.
                - **Dataset:** Combinación de ricos datos internos del cliente con fuentes de datos externas para entrenar y mejorar los modelos de IA.""")


    with st.expander("#### Expansión del Equipo"):
        st.write("""
                - **Equipo Actual**:
                  - *Marketing*: Estrategias de mercado y captación de clientes.
                  - *Product Owner*: Alineación del producto con necesidades del cliente.
                  - *Analista de Datos/Negocio*: Análisis de datos para toma de decisiones.
                  - *Especialista en PYMEs*: Conocimiento del segmento de autónomos.
                - **Nuevas Incorporaciones**:
                  - *Analistas de Datos de Riesgo*: Mejorar evaluación de la viabilidad financiera.
                  - *Data Engineer*: Mantener y escalar infraestructura de datos.
                  - *Data Scientist*: Desarrollo de modelos predictivos con IA y Machine Learning.
                """)

    with st.expander("#### Colaboración con Stakeholders y Optimización de la Infraestructura"):
        st.write("""
                - **Colaboración con Stakeholders**:
                  - Cooperación con áreas de Hipotecas, Riesgos, y TI para alinear estrategias y objetivos.
                  - Relación continua con reguladores para asegurar cumplimiento y aprovechar regulaciones.
                - **Optimización de la Infraestructura**:
                  - Uso de infraestructura en la nube para análisis y seguridad de datos.
                  - Implementación de soluciones de IA para optimizar procesos y decisiones.
                """)

    with st.expander("#### Gestión de Datos"):
        st.write("""
                **Uso de Datos Internos y Externos**:
                - **Acceso a Datos Internos**: Utilizamos una amplia base de datos internos que incluye historiales de transacciones, comportamientos de pago, perfiles demográficos y datos de interacciones anteriores con el banco. Esto nos permite realizar análisis personalizados y profundamente informados, identificando tendencias y patrones que guían el desarrollo de productos y la toma de decisiones estratégicas.
                
                - **Enriquecimiento con Datos Externos**: Complementamos nuestros datos internos con información proveniente de fuentes externas como registros comerciales, bases de datos de crédito y estudios de mercado. Esto nos ayuda a obtener una vista más completa del entorno económico y financiero en el que operan nuestros clientes, mejorando la precisión de nuestros modelos predictivos y la eficacia de nuestras estrategias de riesgo y marketing.
                
                - **Integración y Sincronización de Datos**: Aseguramos que la información de diversas fuentes se integre de manera coherente y esté actualizada en tiempo real. Esto es crucial para mantener la integridad de los datos y para proporcionar una base sólida para todas nuestras operaciones analíticas y decisiones automatizadas.
                
                - **Cumplimiento y Seguridad de Datos**: Cumplimos estrictamente con las regulaciones locales e internacionales sobre protección de datos. Implementamos medidas de seguridad avanzadas para proteger la información contra accesos no autorizados y aseguramos que el uso de datos se maneje con la máxima ética y responsabilidad.
                """)


