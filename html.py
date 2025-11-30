import streamlit as st

# Configuração da página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed"
)

tab0, tab1, tab2, tab3 = st.tabs(["Conceito", "webPreview", "Proposta", "Desenvolvimento"])

with tab0:
    with st.container(horizontal=False):

        st.title("🎯 Objetivo geral")

        st.header("""
        Plataforma web para gestão condominial, com foco em:
        """)

        st.checkbox("Website moderno", value=True)
        st.checkbox("Convivência comunitária", value=True)
        st.checkbox("Controle de portaria", value=True)
        st.checkbox("Gestão de áreas comuns e garagem", value=True)
        st.checkbox("Transparência documental", value=True)
        st.checkbox("Banco de prestadores", value=True)
        st.checkbox("Status de unidades", value=True)
        st.checkbox("Eventos, avisos e comunicados", value=True)
        st.checkbox("Relatório de inadimplência", value=True)
        st.checkbox("Relatório de ocupação", value=True)
        
        st.success("Resultado esperado: reduzir fricções operacionais, aumentar a transparência e criar mecanismos de governança.")
    

with tab1:
    # Lê o HTML completo
    with open(r"conds\villa solar\index2.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # Renderiza dentro do Streamlit
    st.components.v1.html(html_code, height=800, scrolling=True)

with tab2:
    # Dados estruturados
    condominos_items = [
        {
            "title": "📇 Cadastro de moradores e ecossistema social",
            "content": [
                "**:blue[Proprietário:]** histórico de votação e presença em assembleias.",
                "**:blue[Morador:]** Gestão de vagas, reservas, perfil de serviços, controle de visitantes.",
                "**:blue[Cadastro básico:]** Dados essenciais (nome, foto, unidade).",
                "**:blue[Marketplace interno:]** Oferta de serviços e produtos entre moradores.",
                "**:blue[Prestadores externos:]** Cadastro e avaliação binária com comentários auditáveis.",
                "**:blue[Funcionários internos:]** Serviços complementares com rastreabilidade.",
                "**:blue[Status de unidades:]** Ocupada, à venda, disponível, em reforma.",
            ],
        },
        {
            "title": "🚪 Portaria e gestão de visitantes",
            "content": [
                "**:blue[Controle de visitantes:]** Pré-cadastro, verificação na portaria e notificações.",
                "**:blue[Recorrentes vs novos:]** Notificações simplificadas para recorrentes; confirmação para novos.",
                "**:blue[Gestão de encomendas:]** Registro de chegada, alertas e lembretes.",
            ],
        },
        {
            "title": "📅 Reserva de áreas comuns e vagas de garagem",
            "content": [
                "**:blue[Agendamento:]** Espaços com calendário de disponibilidade, preços e regras.", 
                "**:blue[Mapeamento:]** Vagas vinculadas às unidades, com mapa intuitivo.",
                "**:blue[Aluguel dinâmico:]** Concessão temporária ou diária entre unidades.",
            ],
        },
    ]

    administracao_items = [
        {
            "title": "👥 Perfis de acesso (RBAC com JWT authentication e SaaS multi-tenant.)",
            "content": [
                "**:blue[SYSADMIN:]** Gestão de condomínios, usuários, auditorias e faturamento.",
                "**:blue[Administrador:]** Inadimplência, avisos, votações e validação de prestadores.",
                "**:blue[Gestor operacional:]** Visitantes, encomendas e manutenção.",
                "**:blue[Portaria:]** Workflow completo com registro fotográfico e atribuição de responsáveis.",
            ],
        },
        {
            "title": "📊 Relatórios e dashboards executivos",
            "content": [
                "**:blue[Ocupação:]** Taxa de ocupação por torre e tipologia.",
                "**:blue[Inadimplência:]** Indicadores por unidade e histórico.",
                "**:blue[Satisfação:]** Avaliações de prestadores e NPS interno.",
                "**:blue[Participação:]** Taxa de presença em assembleias.",
            ],
        },
        {
            "title": "🔗 Integração com sistemas legados e externos",
            "content": [
                "**:blue[API:]** Importação/exportação de dados via CSV/JSON.",
                "**:blue[Padrões:]** Autenticação tokenizada, versionamento de endpoints e validação de esquema.",
                "**:blue[Google:]** Suite para armazenamento e reuniões.",
                "**:blue[WhatsApp:]** Automação de contatos e notificações.",
            ],
        },
        {
            "title": "📑 Inadimplência, assembleias e transparência documental",
            "content": [
                "**:blue[Controle de inadimplência:]** Restrições automáticas para unidades com débitos.",
                "**:blue[Assembleias:]** Integração para reuniões online com gravação e auditoria.",
                "**:blue[Repositório:]** Central de atas e documentos com versionamento.",
                "**:blue[Multas:]** Denúncias anônimas com foto e regras automáticas.",
            ],
        },
    ]

    # Expander Condôminos
    with st.expander("🏡 Condôminos", expanded=False):
        st.info("📌 Módulo voltado para moradores e proprietários.")
        for idx, item in enumerate(condominos_items):
            with st.container():
                st.subheader(item["title"])
                # Divide em duas colunas para leitura mais leve
                col1, col2 = st.columns(2)
                half = len(item["content"]) // 2
                for line in item["content"][:half]:
                    col1.markdown(f"- {line}")
                for line in item["content"][half:]:
                    col2.markdown(f"- {line}")
            # só adiciona divider se não for o último
            if idx < len(condominos_items) - 1:
                st.divider()

    # Expander Administração
    with st.expander("🏢 Administração", expanded=False):
        st.success("✅ Essencial para governança e transparência.")
        for idx, item in enumerate(administracao_items):
            with st.container():
                st.subheader(item["title"])
                for line in item["content"]:
                    st.markdown(f"- {line}")
            if idx < len(administracao_items) - 1:
                st.divider()

with tab3:
    with st.expander("🚀 Desenvolvimento", expanded=True):

        # Estimativa de desenvolvimento
        with st.expander("📅 Estimativa de desenvolvimento"):
            st.markdown("Usuários Administrativos: **:blue[10]**")
            st.markdown("Unidades: **:blue[176]**")
            st.markdown("Tipos de Usuários por Unidade: **:blue[Proprietário] e :blue[Morador]** ")
            st.markdown("Total de :blue[176] Usuários do tipo **:blue[Proprietário] e :blue[176] Usuários do tipo :blue[Morador]** ")
    
            st.header("Expectativa de desenvolvimento: **:blue[3 meses]**")
            st.write("Preço de **:green[R$25]** por unidade para todas as funcionalidades.")
            st.divider()

        # Sistema de recomendação e descontos
        with st.expander("🎯 Recomendações e Parcerias 🤝 "):
            st.markdown("- Desconto por recomendação a outros condomínios ")
            st.markdown("**:green[10%]** a cada 50 unidades que assinarem o plano de 25/unidade.")
            st.markdown("**:green[100%]** de desconto se o recomendado assinar o plano de 25/unidade com :blue[500 ou mais unidades].")

            st.divider()

            st.markdown("- Possibilidade de **:orange[parcerias]** com administrações, seguradoras, construtoras, financeiras, entre outros")
            st.markdown("Adaptação de funcionalidades **:orange[conforme demandas específicas de cada condomínio]**.")
            st.markdown("Flexibilidade para atender **:orange[diferentes perfis de gestão e operação]**.")
            st.markdown("Oferecimento de **:orange[integrações com ferramentas diversas]**.")
            st.markdown("Fornecimento de computadores **:orange[dedicados para portaria e administração]**, com Linux seguro e estável.")
            

    # Rodapé
    st.divider()
    st.caption("Documento de escopo – Gestão Condominial. Este material descreve requisitos, funcionalidades e diretrizes de entrega para o ciclo inicial de produção.")


