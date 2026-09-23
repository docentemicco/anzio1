import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client

# Configurazione pagina e responsive layout
st.set_page_config(
    page_title="I.C. Anzio 1 - Portale Salute, Farmaci & Deleghe",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Connessione protetta a Supabase
@st.cache_resource
def init_supabase() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

try:
    supabase = init_supabase()
except Exception as e:
    st.error(f"Errore di connessione a Supabase. Controlla i Secrets: {e}")
    st.stop()

# CSS Avanzato per UI istituzionale conforme all'I.C. Anzio 1
st.markdown("""
<style>
    /* Intestazione Istituzionale */
    .header-box {
        background: linear-gradient(135deg, #0b192c 0%, #1e3e62 100%);
        border-bottom: 4px solid #f59e0b;
        border-radius: 14px;
        padding: 24px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .header-box .subtext {
        font-size: 0.8rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #93c5fd;
        font-weight: 600;
    }
    .header-box h1 {
        margin: 6px 0;
        font-size: 1.85rem;
        font-weight: 800;
        color: #ffffff;
    }
    .header-box .desc {
        font-size: 0.95rem;
        color: #e0f2fe;
    }
    
    /* Card e Sezioni */
    .stCard {
        background-color: #ffffff;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        padding: 16px;
        margin-bottom: 12px;
    }
    
    /* Badge personalizzati */
    .badge-grave {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid #fecaca;
    }
    .badge-farmaco {
        background-color: #e0e7ff;
        color: #3730a3;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid #c7d2fe;
    }
    .badge-delega {
        background-color: #d1fae5;
        color: #065f46;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        border: 1px solid #a7f3d0;
    }
</style>
""", unsafe_allow_html=True)

# Banner Istituzionale
st.markdown("""
<div class="header-box">
    <div class="subtext">Ministero dell'Istruzione e del Merito • Ambito Territoriale Lazio</div>
    <h1>Istituto Comprensivo Anzio 1</h1>
    <div class="desc">Portale Istituzionale di Sicurezza: Segnalazione Allergie, Terapie e Deleghe di Ritiro</div>
</div>
""", unsafe_allow_html=True)

# Navigazione
ruolo = st.sidebar.radio("Seleziona Ambiente:", ["👨‍👩‍👧 Accesso Famiglie", "🔒 Area Riservata Docenti"])

PLESSI = [
    "Plesso Falcone - Via Ambrosini",
    "Plesso Ambrosini - Via Ambrosini",
    "Plesso Acqua del Turco (Centrale)",
    "Scuola Infanzia Saragat"
]

# ========================================================
# 1. ACCESSO FAMIGLIE
# ========================================================
if ruolo == "👨‍👩‍👧 Accesso Famiglie":
    st.info("ℹ️ **Modulo Flessibile**: I dati anagrafici base sono obbligatori. Le sezioni per **Allergie**, **Farmaci** e **Deleghe** sono facoltative: attiva solo quelle necessarie per tuo/a figlio/a.")

    with st.form("form_studente", clear_on_submit=True):
        st.markdown("### 1. Dati Essenziali Studente e Genitore")
        c1, c2 = st.columns(2)
        cognome = c1.text_input("Cognome Alunno/a *", placeholder="es. Rossi")
        nome = c2.text_input("Nome Alunno/a *", placeholder="es. Leonardo")

        c3, c4 = st.columns(2)
        plesso = c3.selectbox("Plesso Scolastico *", PLESSI)
        classe = c4.text_input("Classe e Sezione *", placeholder="es. 1A, 2B, 3C")

        c5, c6 = st.columns(2)
        genitore = c5.text_input("Nome e Cognome Genitore/Tutore *", placeholder="es. Mario Rossi (Padre)")
        telefono = c6.text_input("Recapito Telefonico Principale *", placeholder="es. +39 340 1234567")

        st.markdown("---")
        st.markdown("### 2. Allergie o Intolleranze (Facoltativo)")
        ha_allergie = st.toggle("L'alunno/a presenta allergie o intolleranze note?", value=False)
        
        tipo_allergia = ""
        gravita = "Nessuna"
        farmaco_salvavita = ""
        
        if ha_allergie:
            col_a1, col_a2 = st.columns(2)
            tipo_allergia = col_a1.text_area("Descrizione allergene (alimenti, punture, farmaci) *", placeholder="es. Arachidi, derivati lattiero-caseari, ecc.")
            gravita = col_a2.selectbox("Livello di Gravità", [
                "Lieve (fastidio cutaneo lieve)",
                "Moderata (disturbi gastro/cutanei)",
                "Grave (Rischio Anafilassi / Terapia urgente)"
            ])
            farmaco_salvavita = st.text_input("Eventuale farmaco salvavita da usare in emergenza", placeholder="es. Autoiniettore Fastjekt depositato in infermeria")

        st.markdown("---")
        st.markdown("### 3. Farmaci e Terapie in Orario Scolastico (Facoltativo)")
        ha_farmaci = st.toggle("L'alunno/a deve assumere farmaci durante l'orario scolastico?", value=False)
        dettagli_farmaco = ""
        if ha_farmaci:
            dettagli_farmaco = st.text_area("Specificare nome farmaco, orario, dosaggio e piano di somministrazione *", placeholder="es. Ventolin 2 spruzzi al bisogno con certificato medico depositato")

        st.markdown("---")
        st.markdown("### 4. Deleghe di Uscita e Ritiro Studente (Facoltativo)")
        ha_deleghe = st.toggle("Desideri autorizzare soggetti terzi al ritiro oltre ai genitori?", value=False)
        
        delegati_list = []
        if ha_deleghe:
            st.caption("Per ogni persona delegata è obbligatorio indicare Nome, Cognome e Numero di Carta d'Identità.")
            num_delegati = st.number_input("Quante persone desideri delegare?", min_value=1, max_value=5, value=1)
            for i in range(int(num_delegati)):
                st.markdown(f"**Delegato #{i+1}**")
                cd1, cd2, cd3, cd4 = st.columns(4)
                d_nome = cd1.text_input(f"Nome #{i+1}", key=f"dn_{i}")
                d_cognome = cd2.text_input(f"Cognome #{i+1}", key=f"dcg_{i}")
                d_par = cd3.text_input(f"Parentela #{i+1}", placeholder="es. Nonno, Zio", key=f"dp_{i}")
                d_ci = cd4.text_input(f"N° Carta d'Identità #{i+1} *", placeholder="es. CA12345AA", key=f"dci_{i}")
                
                if d_nome.strip() and d_cognome.strip() and d_ci.strip():
                    delegati_list.append({
                        "nome": f"{d_nome.strip().title()} {d_cognome.strip().title()}",
                        "parentela": d_par.strip() or "N/D",
                        "ci": d_ci.strip().upper()
                    })

        st.markdown("---")
        st.markdown("### 5. Conferma e Privacy")
        consenso = st.checkbox("Confermo la veridicità dei dati inseriti e autorizzo il trattamento per le finalità istituzionali di sicurezza scolastica ai sensi dell'Art. 9 GDPR UE 2016/679. *")

        submitted = st.form_submit_button("📤 Trasmetti Fascicolo all'Istituto Anzio 1", use_container_width=True)
        if submitted:
            if not cognome.strip() or not nome.strip() or not classe.strip() or not genitore.strip() or not telefono.strip():
                st.error("I campi contrassegnati dall'asterisco (*) sono obbligatori.")
            elif ha_allergie and not tipo_allergia.strip():
                st.error("Hai attivato la sezione allergie: specifica l'allergene o disattiva il toggle.")
            elif ha_farmaci and not dettagli_farmaco.strip():
                st.error("Hai attivato la somministrazione farmaci: indica il farmaco o disattiva il toggle.")
            elif not consenso:
                st.error("È necessario accettare la clausola privacy per procedere.")
            else:
                record = {
                    "cognome": cognome.strip().title(),
                    "nome": nome.strip().title(),
                    "plesso": plesso,
                    "classe": classe.strip().upper(),
                    "genitore": genitore.strip().title(),
                    "telefono": telefono.strip(),
                    "ha_allergie": ha_allergie,
                    "tipo_allergia": tipo_allergia.strip() if ha_allergie else "Nessuna allergia segnalata",
                    "gravita_allergia": gravita if ha_allergie else "Nessuna",
                    "farmaco_salvavita": farmaco_salvavita.strip() if ha_allergie else "N/A",
                    "ha_farmaci": ha_farmaci,
                    "dettagli_farmaco": dettagli_farmaco.strip() if ha_farmaci else "Nessun farmaco prescritto",
                    "deleghe": delegati_list
                }
                try:
                    supabase.table("alunni_salute_deleghe").insert(record).execute()
                    st.success(f"✅ Fascicolo di {nome} {cognome} trasmesso con successo alla segreteria dell'I.C. Anzio 1!")
                except Exception as err:
                    st.error(f"Errore durante il salvataggio su Supabase: {err}")

# ========================================================
# 2. AREA RISERVATA DOCENTI
# ========================================================
else:
    st.subheader("🔒 Area Riservata Personale Docente & Segreteria")
    PASSWORD_CORRETTA = st.secrets.get("DOCENTI_PASSWORD", "Anzio1Docenti#")
    
    pwd = st.text_input("Inserisci la password di autorizzazione:", type="password")
    if pwd == PASSWORD_CORRETTA:
        st.success("Accesso autorizzato - Trattamento dati protetto ex D.Lgs 196/2003.")
        
        try:
            res = supabase.table("alunni_salute_deleghe").select("*").order("cognome").execute()
            records = res.data or []
        except Exception as e:
            st.error(f"Errore lettura dati: {e}")
            records = []

        if not records:
            st.info("Nessuna scheda registrata al momento nel database.")
        else:
            # Indicatori Rapidi (KPI)
            totali = len(records)
            gravi = sum(1 for r in records if "Grave" in r.get("gravita_allergia", ""))
            solo_deleghe = sum(1 for r in records if not r.get("ha_allergie") and not r.get("ha_farmaci") and len(r.get("deleghe") or []) > 0)
            
            k1, k2, k3 = st.columns(3)
            k1.metric("Fascicoli Alunni", totali)
            k2.metric("Allergie Gravi", gravi)
            k3.metric("Solo Deleghe (No Allergie)", solo_deleghe)

            st.markdown("---")
            # Filtri di ricerca
            c_f1, c_f2 = st.columns(2)
            filtro_plesso = c_f1.selectbox("Filtra per Plesso:", ["Tutti i Plessi"] + PLESSI)
            query = c_f2.text_input("Cerca per Cognome Alunno o N° Documento Delegato:").strip().lower()

            dati_filtrati = records
            if filtro_plesso != "Tutti i Plessi":
                dati_filtrati = [r for r in dati_filtrati if r.get("plesso") == filtro_plesso]
            if query:
                dati_filtrati = [
                    r for r in dati_filtrati
                    if query in r.get("cognome", "").lower()
                    or query in r.get("nome", "").lower()
                    or any(query in d.get("ci", "").lower() or query in d.get("nome", "").lower() for d in (r.get("deleghe") or []))
                ]

            st.caption(f"Visualizzazione di **{len(dati_filtrati)}** alunni.")

            # Elenco Schede Alunno
            for r in dati_filtrati:
                titolo = f"{r['cognome'].upper()} {r['nome']} — Classe {r['classe']} ({r['plesso'].split(' - ')[0]})"
                with st.expander(titolo):
                    col_sx, col_dx = st.columns(2)
                    with col_sx:
                        st.markdown("**Contatti Genitori:**")
                        st.write(f"• Referente: **{r.get('genitore')}**")
                        st.write(f"• Telefono Reperibile: **{r.get('telefono')}**")
                        
                        st.markdown("**Quadro Sanitario:**")
                        if r.get("ha_allergie"):
                            st.markdown(f"<span class='badge-grave'>⚠️ Allergia: {r.get('tipo_allergia')}</span>", unsafe_allow_html=True)
                            st.write(f"Gravità: **{r.get('gravita_allergia')}**")
                            if r.get("farmaco_salvavita") and r.get("farmaco_salvavita") != "N/A":
                                st.error(f"🚑 Farmaco Emergenza: {r.get('farmaco_salvavita')}")
                        else:
                            st.write("✅ Nessuna allergia segnalata.")

                        if r.get("ha_farmaci"):
                            st.markdown(f"<span class='badge-farmaco'>💊 Terapia: {r.get('dettagli_farmaco')}</span>", unsafe_allow_html=True)

                    with col_dx:
                        st.markdown("**Deleghe al Ritiro:**")
                        deleghe = r.get("deleghe") or []
                        if deleghe:
                            for d in deleghe:
                                st.markdown(f"""
                                <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:8px; padding:8px; margin-bottom:6px;">
                                    <b>{d.get('nome')}</b> ({d.get('parentela', 'N/D')})<br>
                                    <span style="font-family:monospace; background:#fef3c7; color:#78350f; padding:2px 6px; border-radius:4px; font-weight:bold;">
                                        Doc: {d.get('ci')}
                                    </span>
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.write("Solo genitori autorizzati al ritiro (nessuna delega inserita).")
    elif pwd != "":
        st.error("Password errata. Accesso riservato al personale dell'istituto.")
