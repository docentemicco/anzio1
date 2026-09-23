import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client

# ==========================================
# 0. CONFIGURAZIONE E CONNESSIONE SUPABASE
# ==========================================
st.set_page_config(
    page_title="I.C. Anzio 1 - Portale Salute & Deleghe",
    page_icon="🏫",
    layout="wide"
)

# Connessione al client Supabase tramite Secrets
@st.cache_resource
def get_supabase_client() -> Client:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

try:
    supabase = get_supabase_client()
except Exception as e:
    st.error("Errore di configurazione del database Supabase. Verifica i parametri in secrets.toml.")
    st.stop()

# Stile Istituzionale Anzio 1
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-bottom: 25px;
    }
    .badge-urgent {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 4px 8px;
        border-radius: 6px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Intestazione Ufficiale
st.markdown("""
<div class="main-header">
    <div style="font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase; opacity: 0.85;">
        Ministero dell'Istruzione e del Merito • Ambito Territoriale Lazio
    </div>
    <h2 style="margin: 5px 0 0 0; color: white;">Istituto Comprensivo Anzio 1</h2>
    <div style="font-size: 0.95rem; opacity: 0.9;">Portale Istituzionale Salute, Farmaci a Scuola e Deleghe al Ritiro</div>
</div>
""", unsafe_allow_html=True)

ruolo = st.sidebar.radio("Seleziona Sezione:", ["👨‍👩‍👧 Portale Famiglie (Inserimento)", "🔒 Area Riservata Docenti"])

PLESSI = [
    "Plesso Falcone - Via Ambrosini (Primaria / Infanzia)",
    "Plesso Ambrosini - Via Ambrosini (Secondaria 1° Grado)",
    "Plesso Acqua del Turco (Primaria / Infanzia)",
    "Plesso Saragat (Primaria)"
]

# ==========================================
# 1. PORTALE FAMIGLIE (INSERIMENTO SUPABASE)
# ==========================================
if ruolo == "👨‍👩‍👧 Portale Famiglie (Inserimento)":
    st.subheader("Modulo di Comunicazione Sanitaria & Deleghe")
    st.info("Compila solo i dati necessari. I campi per allergie, farmaci e deleghe sono facoltativi.")

    with st.form("form_studente", clear_on_submit=True):
        st.markdown("#### 1. Dati Anagrafici Alunno/a")
        c1, c2 = st.columns(2)
        cognome = c1.text_input("Cognome Alunno/a *")
        nome = c2.text_input("Nome Alunno/a *")
        
        c3, c4 = st.columns(2)
        plesso = c3.selectbox("Plesso Scolastico *", PLESSI)
        classe = c4.text_input("Classe e Sezione * (es. 1ª A, 3ª C)")

        st.markdown("#### 2. Recapito Genitore / Tutore")
        cg1, cg2 = st.columns(2)
        genitore = cg1.text_input("Nome e Cognome Genitore/Tutore *")
        telefono = cg2.text_input("Recapito Telefonico di Emergenza *")

        st.markdown("---")
        st.markdown("#### 3. Allergie o Intolleranze")
        ha_allergie = st.toggle("L'alunno/a presenta allergie o intolleranze note?", value=False)
        
        tipo_allergia = ""
        gravita = "Nessuna"
        farmaco_salvavita = ""
        
        if ha_allergie:
            col_a1, col_a2 = st.columns(2)
            tipo_allergia = col_a1.text_area("Descrizione allergene (alimenti, punture, farmaci) *")
            gravita = col_a2.selectbox("Livello di Gravità", [
                "Lieve (fastidio o reazioni lievi)",
                "Moderata (richiede monitoraggio)",
                "Grave (Rischio Anafilassi / Terapia d'urgenza)"
            ])
            farmaco_salvavita = st.text_input("Eventuale farmaco salvavita (es. Autoiniettore di Adrenalina)")

        st.markdown("---")
        st.markdown("#### 4. Assunzione Farmaci / Terapie")
        ha_farmaci = st.toggle("L'alunno/a deve assumere farmaci durante l'orario scolastico?", value=False)
        dettagli_farmaco = ""
        if ha_farmaci:
            dettagli_farmaco = st.text_area("Specificare nome farmaco, orario, dosaggio e modalità di somministrazione *")

        st.markdown("---")
        st.markdown("#### 5. Deleghe di Uscita al Ritiro")
        ha_deleghe = st.toggle("Desideri autorizzare soggetti terzi al ritiro oltre ai genitori?", value=False)
        
        delegati_list = []
        if ha_deleghe:
            num_delegati = st.number_input("Numero di persone da delegare", min_value=1, max_value=5, value=1)
            for i in range(int(num_delegati)):
                st.markdown(f"**Delegato #{i+1}**")
                cd1, cd2, cd3, cd4 = st.columns(4)
                d_nome = cd1.text_input(f"Nome e Cognome #{i+1}", key=f"dn_{i}")
                d_par = cd2.text_input(f"Parentela / Relazione #{i+1}", key=f"dp_{i}")
                d_ci = cd3.text_input(f"N° Carta d'Identità #{i+1} *", key=f"dc_{i}")
                d_tel = cd4.text_input(f"Telefono #{i+1}", key=f"dt_{i}")
                if d_nome.strip() and d_ci.strip():
                    delegati_list.append({
                        "nome": d_nome.strip(),
                        "parentela": d_par.strip(),
                        "ci": d_ci.strip().upper(),
                        "tel": d_tel.strip()
                    })

        st.markdown("---")
        consenso = st.checkbox("Dichiaro che i dati forniti sono veritieri e autorizzo il trattamento ai sensi dell'Art. 9 del GDPR.")

        submitted = st.form_submit_button("📤 Invia Scheda Ufficiale", use_container_width=True)
        if submitted:
            if not cognome.strip() or not nome.strip() or not classe.strip() or not genitore.strip() or not telefono.strip():
                st.error("Compila tutti i campi anagrafici contrassegnati con l'asterisco (*).")
            elif not consenso:
                st.error("È necessario accettare la clausola sul trattamento dati prima di inviare.")
            else:
                dati_da_salvare = {
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
                    # Inserimento record su Supabase
                    risposta = supabase.table("alunni_salute_deleghe").insert(dati_da_salvare).execute()
                    st.success(f"✅ Scheda di {nome} {cognome} registrata con successo nel database protetto dell'Istituto!")
                except Exception as err:
                    st.error(f"Errore durante il salvataggio su Supabase: {err}")

# ==========================================
# 2. AREA RISERVATA DOCENTI (LETTURA SUPABASE)
# ==========================================
else:
    st.subheader("🔒 Accesso Riservato Personale Docente & Segreteria")
    
    PASSWORD_DOCENTI = st.secrets.get("DOCENTI_PASSWORD", "Anzio1Docenti#")
    pwd = st.text_input("Inserisci la password di autorizzazione docente:", type="password")
    
    if pwd == PASSWORD_DOCENTI:
        st.success("Accesso autorizzato - Connesso al database crittografato Supabase.")
        
        # Recupero dati da Supabase
        try:
            response = supabase.table("alunni_salute_deleghe").select("*").order("cognome").execute()
            records = response.data
        except Exception as e:
            st.error(f"Errore nel recupero dei dati da Supabase: {e}")
            records = []

        if not records:
            st.info("Nessuna scheda presente nel database.")
        else:
            col_f1, col_f2 = st.columns(2)
            plesso_filtro = col_f1.selectbox("Filtra per Plesso:", ["Tutti i Plessi"] + PLESSI)
            ricerca = col_f2.text_input("Cerca per Cognome, Nome o N° Carta d'Identità Delegato:")
            
            # Filtri logici
            dati_mostrati = records
            if plesso_filtro != "Tutti i Plessi":
                dati_mostrati = [r for r in dati_mostrati if r.get("plesso") == plesso_filtro]
            
            if ricerca.strip():
                q = ricerca.strip().lower()
                dati_mostrati = [
                    r for r in dati_mostrati 
                    if q in r.get("cognome", "").lower() 
                    or q in r.get("nome", "").lower()
                    or any(q in d.get("ci", "").lower() or q in d.get("nome", "").lower() for d in (r.get("deleghe") or []))
                ]

            st.write(f"Risultati trovati: **{len(dati_mostrati)}**")

            # Visualizzazione schede alunni
            for r in dati_mostrati:
                titolo_expander = f"📋 {r['cognome'].upper()} {r['nome']} - Classe {r['classe']} ({r['plesso'].split(' - ')[0]})"
                with st.expander(titolo_expander):
                    c_left, c_right = st.columns(2)
                    with c_left:
                        st.markdown("**Contatti Famiglia:**")
                        st.write(f"• Genitore Referente: **{r.get('genitore')}**")
                        st.write(f"• Telefono: **{r.get('telefono')}**")
                        
                        st.markdown("**Situazione Sanitaria:**")
                        if r.get("ha_allergie"):
                            st.markdown(f"<span class='badge-urgent'>⚠️ Allergia: {r.get('tipo_allergia')}</span>", unsafe_allow_html=True)
                            st.write(f"Gravità: **{r.get('gravita_allergia')}**")
                            if r.get("farmaco_salvavita") and r.get("farmaco_salvavita") != "N/A":
                                st.error(f"🚑 Farmaco Emergenza: {r.get('farmaco_salvavita')}")
                        else:
                            st.write("✅ Nessuna allergia segnalata")

                        if r.get("ha_farmaci"):
                            st.warning(f"💊 Farmaco in orario scolastico: {r.get('dettagli_farmaco')}")

                    with c_right:
                        st.markdown("**Deleghe al Ritiro Autorizzate:**")
                        deleghe = r.get("deleghe") or []
                        if deleghe:
                            for d in deleghe:
                                st.info(f"👤 **{d.get('nome')}** ({d.get('parentela', 'N/D')})\n\n🪪 **C.I.: {d.get('ci')}** | 📞 Tel: {d.get('tel', 'N/D')}")
                        else:
                            st.write("Nessuna persona delegata (uscita solo con i genitori).")
    elif pwd != "":
        st.error("Password errata. Accesso negato.")
