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
    with open(r"D:\.py\dotaMind\conds\villa solar\index2.html", "r", encoding="utf-8") as f:
        html_code = f.read()

    # Renderiza dentro do Streamlit
    st.components.v1.html(html_code, height=800, scrolling=True)

    # Cabeçalho
    st.title("Plataforma de gestão condominial – MVP")
    st.caption("Documento de escopo técnico e análise estratégica | Atualizado em 26/11/2025")

with tab2:
    # Dados estruturados: cada item será renderizado por for loop dentro de containers
    condominos_items = [
        {
            "title": "Cadastro de moradores e ecossistema social",
            "content": [
                "**Proprietário:** histórico de votação e de presença em assembléias.",
                "**Morador:** Gestão de vagas, visualização da vizinhança, reservas,perfil de serviços, controle de visitantes da unidade.",
                "**Cadastro básico e identificação:** Dados essenciais (nome, foto, unidade). Opção opt-in para moradores, mantendo visibilidade para administradores.",
                "**Marketplace interno:** Espaço para oferta de serviços (ex.: contabilidade, assistência técnica, manicure) e produtos (ex.: alimentos, bebidas), visível a administradores e moradores.",
                "**Prestadores externos:** Cadastro e avaliação binária (Recomendado/Não recomendado) com comentários (anônimos), auditáveis (e visíveis)pelos administradores.",
                "**Funcionários internos:** Oferta de serviços complementares com rastreabilidade de execução e histórico.",
                "**Status de unidades:** Indicador (ocupada, à venda, disponível, em reforma) com regras operacionais (ex.: restrição de aluguel de vagas e notificações específicas para unidades desocupadas).",
            ],
        },
        {
            "title": "Portaria e gestão de visitantes",
            "content": [
                "**Controle de visitantes:** Pré-cadastro de convidados, verificação na portaria e notificações via WhatsApp ou interfone, com rastreabilidade de entradas.",
                "**Visitantes recorrentes vs novos:** Notificações simplificadas para recorrentes; confirmação por interfone para novos visitantes, elevando a segurança.",
                "**Gestão de encomendas:** Registro de chegada, alertas automáticos e lembrete via interfone em caso de não retirada.",
            ],
        },
        {
            "title": "Reserva de áreas comuns",
            "content": [
                "Módulo de agendamento de espaços com calendário de disponibilidade, preços, regras e restrições.",
                "Integração com agenda de assembleias e reuniões administrativas.",
            ],
        },
        {
            "title": "Gestão de vagas de garagem",
            "content": [
                "**Mapeamento e visualização:** Vagas vinculadas diretamente às unidades, com mapa de ocupação intuitivo para identificação rápida e operação eficiente.",
                "**Aluguel dinâmico entre moradores:** Concessão temporária ou diária entre unidades, com controle de datas, precificação dinâmica.",
            ],
        },
    ]

    administracao_items = [
        {
            "title": "Perfis de acesso (SYSADMIN, Administrador, Gestor operacional)",
            "content": [
                "**SYSADMIN:** Gestão de condomínios (criação, exclusão, suspensão), administração de usuários, auditorias e faturamento.",
                "**Administrador do condomínio:** Inadimplência, avisos, moderação de votações e validação de prestadores.",
                "**Gestor operacional:** Confirmação de visitantes, registro de encomendas e solicitações de manutenção.",
                "Modelo RBAC (Role-Based Access Control) com autenticação via JWT e conformidade multi-tenant SaaS.",
            ],
        },
        {
            "title": "Relatórios e dashboards executivos (KPIs)",
            "content": [
                "**Ocupação:** Taxa de ocupação por torre e tipologia.",
                "**Inadimplência:** Indicadores por unidade e histórico por período.",
                "**Satisfação:** Avaliações de prestadores e NPS interno.",
                "**Participação:** Taxa de presença em assembleias.",
            ],
        },
        {
            "title": "Integração com sistemas legados",
            "content": [
                "API para importação e exportação de dados (moradores, unidades, inadimplência, histórico financeiro) via CSV/JSON.",
                "**Padrões:** autenticação tokenizada, versionamento de endpoints e validação de esquema para garantir integridade.",
            ],
        },
        {
            "title": "Inadimplência, assembleias e transparência documental",
            "content": [
                "**Controle de inadimplência:** Detecção automatizada e aplicação de restrições (voto, reservas, aluguel de espaços/vagas) para unidades com débitos.",
                "**Assembleias:** Possibilidade de integração para reuniões online com gravação, transcrição, controle de participantes e auditoria de presenças.",
                "**Repositório de documentos:** Central de atas, documentos administrativos, prestações de contas e relatórios, com versionamento e trilha de auditoria.",
                "**Multas e infrações:** Denúncias anônimas com foto e contexto, histórico por unidade e regras para multas automáticas em casos recorrentes.",
            ],
        },
        {
            "title": "Sistema operacional da portaria",
            "content": [
                "Hardware dedicado com Linux em modo Kiosk, acesso exclusivo ao aplicativo de portaria e restrição de funções não relacionadas.",
                "**Manutenção e solicitações:** Workflow completo (aberto, em andamento, concluído), registro fotográfico e atribuição clara de responsáveis.",
            ],
        },
    ]

    with st.expander("🏡 Condôminos", expanded=True):
        for item in condominos_items:
            with st.container():
                    st.subheader(item["title"])
                    for line in item["content"]:
                        st.markdown(f"- {line}")


    with st.expander("🏢 Administração", expanded=True):
        for item in administracao_items:
            with st.container():
                st.subheader(item["title"])
                for line in item["content"]:
                    st.markdown(f"- {line}")

    with tab3:
        tasks = [
            {
                "title": "Estimativa de desenvolvimento",
                "content": [
                    "Prazo do MVP: aproximadamente 3 meses, distribuídos em 4 sprints.",
                    "**Critérios de sucesso:**",
                    "Onboarding funcional (API e importadores CSV/JSON) com preservação de histórico.",
                    "RBAC operante e portaria em modo Kiosk estável.",
                    "Dashboards com KPIs prioritários e fluxo de reservas publicado.",
                    "Módulo de inadimplência com regras de bloqueio e trilha de auditoria.",
                ],
            }
        ]

        with st.expander("Desenvolvimento", expanded=True):
            for item in tasks:
                with st.container():
                    st.subheader(item["title"])
                    # Renderiza a primeira linha como texto normal e as demais como lista
                    if item["content"]:
                        st.write(item["content"][0])  # texto introdutório
                        for line in item["content"][1:]:
                            st.markdown(f"- {line}")


    # Rodapé
    st.divider()
    st.caption("Documento de escopo – Gestão Condominial. Este material descreve requisitos, funcionalidades e diretrizes de entrega para o ciclo inicial de produção.")
