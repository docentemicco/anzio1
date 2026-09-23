import React, { useState, useMemo } from 'react';
import {
  Shield,
  ShieldAlert,
  ShieldCheck,
  AlertTriangle,
  Pill,
  Users,
  UserCheck,
  FileText,
  Lock,
  LogOut,
  Search,
  Filter,
  Plus,
  Trash2,
  Printer,
  ChevronRight,
  School,
  HeartPulse,
  Phone,
  CheckCircle2,
  Clock,
  IdCard,
  Eye,
  Info,
  Calendar,
  AlertCircle,
  ToggleLeft,
  ToggleRight,
  Check
} from 'lucide-react';

const INITIAL_STUDENTS = [
  {
    id: "anzio-std-001",
    firstName: "Leonardo",
    lastName: "Rossi",
    birthDate: "2015-04-12",
    classRoom: "3A",
    campus: "Plesso Acqua del Turco",
    parentName: "Marco Rossi (Padre)",
    parentPhone: "+39 340 1234567",
    parentEmail: "marco.rossi@email.it",
    updatedAt: "2026-09-18 10:30",
    hasAllergies: true,
    allergies: [
      {
        id: "a1",
        type: "Alimentare",
        substance: "Arachidi e frutta a guscio",
        severity: "grave",
        emergencyPlan: "Somministrazione immediata autoiniettore adrenalina (Fastjekt) situato in infermeria. Chiamare 118."
      }
    ],
    hasMedications: true,
    medications: [
      {
        id: "m1",
        name: "Ventolin spray",
        dosage: "2 spruzzi al bisogno",
        timing: "In caso di crisi asmatica o respiro sibilante",
        doctorAuth: true,
        notes: "Depositato in presidenza con certificato medico del 10/09/2026."
      }
    ],
    hasDelegates: true,
    delegates: [
      {
        id: "d1",
        firstName: "Carla",
        lastName: "Bianchi",
        relationship: "Nonna materna",
        idCardNumber: "CA98765ZX",
        phone: "+39 333 9876543",
        note: "Disponibile dal lunedì al venerdì"
      }
    ]
  },
  {
    id: "anzio-std-002",
    firstName: "Giulia",
    lastName: "Moretti",
    birthDate: "2017-05-14",
    classRoom: "1A",
    campus: "Plesso Ambrosini",
    parentName: "Laura Ferri (Madre)",
    parentPhone: "+39 339 5544332",
    parentEmail: "laura.ferri@email.it",
    updatedAt: "2026-09-22 11:20",
    hasAllergies: false,
    allergies: [],
    hasMedications: false,
    medications: [],
    hasDelegates: true,
    delegates: [
      {
        id: "d-moretti-1",
        firstName: "Roberto",
        lastName: "Moretti",
        relationship: "Zio maggiorenne",
        idCardNumber: "AY887766K",
        phone: "+39 331 4455667",
        note: "Ritiro ordinario ore 16:30"
      },
      {
        id: "d-moretti-2",
        firstName: "Franca",
        lastName: "Galli",
        relationship: "Nonna paterna",
        idCardNumber: "CB123499X",
        phone: "+39 347 1122334",
        note: "Tutti i giorni feriali"
      }
    ]
  },
  {
    id: "anzio-std-003",
    firstName: "Sofia",
    lastName: "Esposito",
    birthDate: "2017-08-22",
    classRoom: "1B",
    campus: "Plesso Falcone",
    parentName: "Elena De Angelis (Madre)",
    parentPhone: "+39 347 8899001",
    parentEmail: "elena.deangelis@email.it",
    updatedAt: "2026-09-15 14:15",
    hasAllergies: true,
    allergies: [
      {
        id: "a3",
        type: "Alimentare",
        substance: "Lattosio e derivati latte",
        severity: "moderata",
        emergencyPlan: "Dieta speciale certificata ASL Roma 6 per mensa. No latticini."
      }
    ],
    hasMedications: false,
    medications: [],
    hasDelegates: false,
    delegates: []
  },
  {
    id: "anzio-std-004",
    firstName: "Matteo",
    lastName: "Mancini",
    birthDate: "2016-02-03",
    classRoom: "2A",
    campus: "Plesso Acqua del Turco",
    parentName: "Roberto Mancini (Padre)",
    parentPhone: "+39 349 4433221",
    parentEmail: "mancini.rob@email.it",
    updatedAt: "2026-09-20 09:00",
    hasAllergies: true,
    allergies: [
      {
        id: "a4",
        type: "Insetti / Veleno",
        substance: "Punture di vespe e api",
        severity: "grave",
        emergencyPlan: "Shock anafilattico possibile. Allertare immediatamente il 118 e il personale formato."
      }
    ],
    hasMedications: true,
    medications: [
      {
        id: "m2",
        name: "Delfosid compresse",
        dosage: "1 compressa ore 12:00",
        timing: "Durante il pasto",
        doctorAuth: true,
        notes: "Terapia autorizzata dal Dirigente Scolastico con protocollo 4812/A."
      }
    ],
    hasDelegates: true,
    delegates: [
      {
        id: "d4",
        firstName: "Maria Teresa",
        lastName: "Marino",
        relationship: "Baby Sitter di famiglia",
        idCardNumber: "EE556677Z",
        phone: "+39 342 9988771",
        note: "Presentarsi con documento"
      }
    ]
  }
];

const CAMPUSES = [
  "Plesso Acqua del Turco (Centrale)",
  "Plesso Falcone",
  "Plesso Ambrosini",
  "Scuola Infanzia Saragat"
];

const CLASSES = ["1A", "1B", "1C", "2A", "2B", "3A", "3B", "3C", "Infanzia Sez. Gialla", "Infanzia Sez. Blu"];

export default function App() {
  const [activeTab, setActiveTab] = useState('parent'); // 'parent' | 'teacher_login' | 'teacher_dashboard'
  const [studentsList, setStudentsList] = useState(INITIAL_STUDENTS);

  // Authentication State for Teachers
  const [teacherAuth, setTeacherAuth] = useState({
    isAuthenticated: false,
    teacherName: "Docente Coordinatore",
    teacherCode: "DOC-ANZIO1"
  });
  const [loginPassword, setLoginPassword] = useState("");
  const [loginCode, setLoginCode] = useState("");
  const [loginError, setLoginError] = useState("");

  // Filters for Teacher Dashboard
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedClass, setSelectedClass] = useState("all");
  const [selectedCampus, setSelectedCampus] = useState("all");
  const [filterType, setFilterType] = useState("all"); // 'all' | 'only_delegates' | 'allergies' | 'severe' | 'meds'
  const [selectedStudentForModal, setSelectedStudentForModal] = useState(null);
  const [isPickupQuickMode, setIsPickupQuickMode] = useState(false);

  // Notification Banner
  const [feedbackMessage, setFeedbackMessage] = useState(null);

  const showNotification = (msg, type = "success") => {
    setFeedbackMessage({ msg, type });
    setTimeout(() => setFeedbackMessage(null), 5000);
  };

  const handleParentFormSubmit = (newStudentRecord) => {
    setStudentsList(prev => [newStudentRecord, ...prev]);
    showNotification("Fascicolo trasmesso con successo all'I.C. Anzio 1. I dati sono stati aggiornati.");
  };

  const handleTeacherLogin = (e) => {
    e.preventDefault();
    if (loginPassword.trim() === "Anzio1Docenti#" || loginPassword.trim() === "Docente2026!") {
      setTeacherAuth({
        isAuthenticated: true,
        teacherName: loginCode ? `Docente (${loginCode.toUpperCase()})` : "Docente di Classe",
        teacherCode: loginCode || "DOC-ANZIO1"
      });
      setActiveTab('teacher_dashboard');
      setLoginError("");
      setLoginPassword("");
      showNotification("Accesso autorizzato all'ambiente riservato docenti.", "info");
    } else {
      setLoginError("Password istituzionale errata. Utilizzare le credenziali fornite per l'I.C. Anzio 1.");
    }
  };

  const handleTeacherLogout = () => {
    setTeacherAuth({ isAuthenticated: false, teacherName: "", teacherCode: "" });
    setActiveTab('parent');
    showNotification("Sessione docente terminata in sicurezza.", "info");
  };

  const filteredStudents = useMemo(() => {
    return studentsList.filter(student => {
      const matchSearch =
        student.firstName.toLowerCase().includes(searchTerm.toLowerCase()) ||
        student.lastName.toLowerCase().includes(searchTerm.toLowerCase()) ||
        student.classRoom.toLowerCase().includes(searchTerm.toLowerCase()) ||
        student.delegates.some(d =>
          `${d.firstName} ${d.lastName}`.toLowerCase().includes(searchTerm.toLowerCase()) ||
          d.idCardNumber.toLowerCase().includes(searchTerm.toLowerCase())
        );

      const matchClass = selectedClass === "all" || student.classRoom === selectedClass;
      const matchCampus = selectedCampus === "all" || student.campus.includes(selectedCampus);

      let matchFilter = true;
      if (filterType === "only_delegates") {
        matchFilter = student.delegates.length > 0 && student.allergies.length === 0 && student.medications.length === 0;
      } else if (filterType === "allergies") {
        matchFilter = student.allergies.length > 0;
      } else if (filterType === "severe") {
        matchFilter = student.allergies.some(a => a.severity === "grave");
      } else if (filterType === "meds") {
        matchFilter = student.medications.length > 0;
      } else if (filterType === "no_allergies") {
        matchFilter = student.allergies.length === 0;
      }

      return matchSearch && matchClass && matchCampus && matchFilter;
    });
  }, [studentsList, searchTerm, selectedClass, selectedCampus, filterType]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 flex flex-col font-sans selection:bg-blue-100 selection:text-blue-900">
      
      {/* HEADER ISTITUZIONALE */}
      <header className="bg-gradient-to-r from-blue-950 via-blue-900 to-indigo-950 text-white border-b-4 border-amber-400 shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
          <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
            
            <div className="flex items-center gap-3.5">
              <div className="w-12 h-12 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 flex items-center justify-center p-2 shadow-inner text-amber-300">
                <School className="w-8 h-8" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xs uppercase tracking-wider font-semibold text-blue-200">
                    Ministero dell'Istruzione e del Merito
                  </span>
                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                  <span className="text-[11px] text-emerald-300 font-medium hidden sm:inline">Servizio Attivo 24/7</span>
                </div>
                <h1 className="text-lg sm:text-xl font-bold tracking-tight text-white flex items-center gap-2">
                  Istituto Comprensivo Anzio 1
                  <span className="text-xs font-normal bg-blue-800/80 text-blue-100 px-2 py-0.5 rounded border border-blue-600/50">
                    Anzio (RM)
                  </span>
                </h1>
                <p className="text-xs text-blue-200/90 font-medium">
                  Portale Istituzionale di Sicurezza: Segnalazione Allergie, Terapie e Deleghe di Ritiro
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2 self-start md:self-auto">
              <button
                onClick={() => setActiveTab('parent')}
                className={`px-3.5 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 ${
                  activeTab === 'parent'
                    ? 'bg-white text-blue-950 shadow-sm'
                    : 'bg-blue-900/60 hover:bg-blue-800 text-blue-100 border border-blue-700/60'
                }`}
              >
                <Users className="w-4 h-4 text-blue-600" />
                Accesso Famiglie
              </button>

              {teacherAuth.isAuthenticated ? (
                <div className="flex items-center gap-2">
                  <button
                    onClick={() => setActiveTab('teacher_dashboard')}
                    className={`px-3.5 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 ${
                      activeTab === 'teacher_dashboard'
                        ? 'bg-amber-400 text-blue-950 shadow-sm'
                        : 'bg-blue-900/60 hover:bg-blue-800 text-amber-200 border border-amber-400/40'
                    }`}
                  >
                    <ShieldCheck className="w-4 h-4 text-amber-600" />
                    Area Docenti
                  </button>
                  <button
                    onClick={handleTeacherLogout}
                    title="Disconnetti docente"
                    className="p-2 rounded-lg bg-red-600/80 hover:bg-red-700 text-white transition-colors"
                  >
                    <LogOut className="w-4 h-4" />
                  </button>
                </div>
              ) : (
                <button
                  onClick={() => setActiveTab('teacher_login')}
                  className={`px-3.5 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 ${
                    activeTab === 'teacher_login'
                      ? 'bg-amber-400 text-blue-950 shadow-sm'
                      : 'bg-blue-900/60 hover:bg-blue-800 text-amber-200 border border-amber-400/40'
                  }`}
                >
                  <Lock className="w-4 h-4 text-amber-300" />
                  Area Riservata Docenti
                </button>
              )}
            </div>
          </div>
        </div>

        <div className="bg-blue-950/90 border-t border-blue-800/60 text-[11px] text-blue-300 px-4 py-1.5">
          <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
            <span className="flex items-center gap-1.5">
              <Shield className="w-3.5 h-3.5 text-emerald-400" />
              Ambiente protetto GDPR art. 9. Modulo flessibile: compila solo le sezioni necessarie.
            </span>
            <span className="font-mono text-blue-200">
              ID Istituto: RMIC8CX00P | Anzio (RM)
            </span>
          </div>
        </div>
      </header>

      {/* Global Toast */}
      {feedbackMessage && (
        <div className="max-w-7xl mx-auto px-4 mt-3 w-full">
          <div
            className={`p-3 rounded-lg text-sm flex items-center justify-between shadow-sm border ${
              feedbackMessage.type === "success"
                ? "bg-emerald-50 text-emerald-900 border-emerald-300"
                : "bg-blue-50 text-blue-900 border-blue-300"
            }`}
          >
            <div className="flex items-center gap-2.5">
              <CheckCircle2 className="w-5 h-5 text-emerald-600 flex-shrink-0" />
              <span>{feedbackMessage.msg}</span>
            </div>
            <button
              onClick={() => setFeedbackMessage(null)}
              className="text-xs font-bold text-slate-500 hover:text-slate-800 px-2"
            >
              Chiudi
            </button>
          </div>
        </div>
      )}

      {/* MAIN VIEW CONTAINER */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {activeTab === 'parent' && (
          <ParentSubmissionView
            onFormSubmit={handleParentFormSubmit}
            campuses={CAMPUSES}
            classes={CLASSES}
          />
        )}

        {activeTab === 'teacher_login' && (
          <TeacherLoginView
            loginPassword={loginPassword}
            setLoginPassword={setLoginPassword}
            loginCode={loginCode}
            setLoginCode={setLoginCode}
            loginError={loginError}
            onSubmit={handleTeacherLogin}
            onBackToParent={() => setActiveTab('parent')}
          />
        )}

        {activeTab === 'teacher_dashboard' && teacherAuth.isAuthenticated && (
          <TeacherDashboardView
            teacherAuth={teacherAuth}
            students={filteredStudents}
            allStudents={studentsList}
            searchTerm={searchTerm}
            setSearchTerm={setSearchTerm}
            selectedClass={selectedClass}
            setSelectedClass={setSelectedClass}
            selectedCampus={selectedCampus}
            setSelectedCampus={setSelectedCampus}
            filterType={filterType}
            setFilterType={setFilterType}
            campuses={CAMPUSES}
            classes={CLASSES}
            onOpenStudentDetail={(student) => setSelectedStudentForModal(student)}
            isPickupQuickMode={isPickupQuickMode}
            setIsPickupQuickMode={setIsPickupQuickMode}
          />
        )}
      </main>

      {/* STUDENT DETAIL MODAL */}
      {selectedStudentForModal && (
        <StudentDetailModal
          student={selectedStudentForModal}
          onClose={() => setSelectedStudentForModal(null)}
        />
      )}

      {/* FOOTER */}
      <footer className="bg-slate-900 text-slate-400 text-xs py-6 border-t border-slate-800 mt-auto">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2 text-slate-300">
            <School className="w-4 h-4 text-amber-400" />
            <span>Istituto Comprensivo Anzio 1 - Via Ambrosini / Acqua del Turco, 00042 Anzio (RM)</span>
          </div>
          <div className="flex items-center gap-4 text-slate-400 text-[11px]">
            <span>Codice Meccanografico: RMIC8CX00P</span>
            <span>•</span>
            <span>Privacy Policy & DPO Scolastico</span>
            <span>•</span>
            <span className="text-emerald-400">Sistema Attivo</span>
          </div>
        </div>
      </footer>
    </div>
  );
}

/* =========================================================================
   PARENT SUBMISSION COMPONENT - CON SEZIONI FACOLTATIVE SMART
   ========================================================================= */
function ParentSubmissionView({ onFormSubmit, campuses, classes }) {
  // Obbligatori: Solo dati anagrafici base
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    birthDate: "",
    classRoom: "1A",
    campus: campuses[0],
    parentName: "",
    parentPhone: "",
    parentEmail: "",
    privacyAccepted: true
  });

  // Toggles Sezioni Facoltative
  const [hasAllergies, setHasAllergies] = useState(false);
  const [hasMedications, setHasMedications] = useState(false);
  const [hasDelegates, setHasDelegates] = useState(false);

  // Dynamic Allergies List
  const [allergies, setAllergies] = useState([]);
  const [currentAllergy, setCurrentAllergy] = useState({
    type: "Alimentare",
    substance: "",
    severity: "moderata",
    emergencyPlan: ""
  });

  // Dynamic Medications List
  const [medications, setMedications] = useState([]);
  const [currentMed, setCurrentMed] = useState({
    name: "",
    dosage: "",
    timing: "",
    notes: ""
  });

  // Dynamic Delegates List (opzionale, vuota o con elementi)
  const [delegates, setDelegates] = useState([]);

  const [validationError, setValidationError] = useState("");
  const [showSuccessCard, setShowSuccessCard] = useState(false);
  const [lastSubmittedStudent, setLastSubmittedStudent] = useState(null);

  // Add Allergy
  const handleAddAllergy = () => {
    if (!currentAllergy.substance.trim()) {
      setValidationError("Inserisci il nome della sostanza o alimento prima di aggiungerlo.");
      return;
    }
    setAllergies([...allergies, { ...currentAllergy, id: "alg-" + Date.now() }]);
    setCurrentAllergy({
      type: "Alimentare",
      substance: "",
      severity: "moderata",
      emergencyPlan: ""
    });
    setValidationError("");
  };

  const handleRemoveAllergy = (id) => {
    setAllergies(allergies.filter(a => a.id !== id));
  };

  // Add Medication
  const handleAddMedication = () => {
    if (!currentMed.name.trim()) {
      setValidationError("Specifica il nome del farmaco prima di aggiungerlo.");
      return;
    }
    setMedications([...medications, { ...currentMed, id: "med-" + Date.now(), doctorAuth: true }]);
    setCurrentMed({
      name: "",
      dosage: "",
      timing: "",
      notes: ""
    });
    setValidationError("");
  };

  const handleRemoveMedication = (id) => {
    setMedications(medications.filter(m => m.id !== id));
  };

  // Add Delegate
  const handleAddDelegate = () => {
    setDelegates([
      ...delegates,
      {
        id: "del-" + Date.now(),
        firstName: "",
        lastName: "",
        relationship: "Parente / Conoscente",
        idCardNumber: "",
        phone: "",
        note: ""
      }
    ]);
  };

  const handleRemoveDelegate = (id) => {
    setDelegates(delegates.filter(d => d.id !== id));
  };

  const handleDelegateChange = (id, field, value) => {
    setDelegates(delegates.map(d => (d.id === id ? { ...d, [field]: value } : d)));
  };

  // Toggle handlers con auto-inizializzazione utile
  const handleToggleDelegates = (enabled) => {
    setHasDelegates(enabled);
    if (enabled && delegates.length === 0) {
      handleAddDelegate();
    }
  };

  // Submit complete record
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validazione SOLO dei campi obbligatori essenziali
    if (!formData.firstName.trim() || !formData.lastName.trim() || !formData.parentName.trim() || !formData.parentPhone.trim()) {
      setValidationError("Compilare i dati anagrafici obbligatori dello studente e il recapito del genitore (contrassegnati con *).");
      return;
    }

    // Se ha attivato le allergie ma non ne ha aggiunta nessuna
    if (hasAllergies && allergies.length === 0) {
      if (currentAllergy.substance.trim()) {
        allergies.push({ ...currentAllergy, id: "alg-" + Date.now() });
      } else {
        setValidationError("Hai indicato che l'alunno soffre di allergie: inserisci almeno un allergene o disattiva la spunta se non presente.");
        return;
      }
    }

    // Se ha attivato i farmaci ma non ne ha aggiunti
    if (hasMedications && medications.length === 0) {
      if (currentMed.name.trim()) {
        medications.push({ ...currentMed, id: "med-" + Date.now(), doctorAuth: true });
      } else {
        setValidationError("Hai indicato l'assunzione di farmaci: indica il nome del farmaco o disattiva l'opzione se non necessario.");
        return;
      }
    }

    // Se ha attivato le deleghe, controlla che quelle compilate abbiano i dati minimi (Nome, Cognome, Carta d'Identità)
    if (hasDelegates) {
      if (delegates.length === 0) {
        setValidationError("Hai selezionato di voler aggiungere delegati: inserisci almeno un nominativo o disattiva la sezione.");
        return;
      }
      const incompleteDelegate = delegates.find(d => !d.firstName.trim() || !d.lastName.trim() || !d.idCardNumber.trim());
      if (incompleteDelegate) {
        setValidationError("Per ogni delegato inserito è obbligatorio specificare Nome, Cognome e Numero Carta d'Identità.");
        return;
      }
    }

    if (!formData.privacyAccepted) {
      setValidationError("È necessario confermare la presa visione del trattamento dati istituzionale.");
      return;
    }

    const finalRecord = {
      id: "anzio-std-" + Date.now(),
      firstName: formData.firstName.trim(),
      lastName: formData.lastName.trim(),
      birthDate: formData.birthDate || "2016-01-01",
      classRoom: formData.classRoom,
      campus: formData.campus,
      parentName: formData.parentName.trim(),
      parentPhone: formData.parentPhone.trim(),
      parentEmail: formData.parentEmail.trim() || "Non indicata",
      updatedAt: new Date().toLocaleString('it-IT'),
      hasAllergies: hasAllergies && allergies.length > 0,
      allergies: hasAllergies ? allergies : [],
      hasMedications: hasMedications && medications.length > 0,
      medications: hasMedications ? medications : [],
      hasDelegates: hasDelegates && delegates.length > 0,
      delegates: hasDelegates ? delegates : []
    };

    setLastSubmittedStudent(finalRecord);
    onFormSubmit(finalRecord);
    setShowSuccessCard(true);
    setValidationError("");
  };

  const resetForm = () => {
    setFormData({
      firstName: "",
      lastName: "",
      birthDate: "",
      classRoom: "1A",
      campus: campuses[0],
      parentName: "",
      parentPhone: "",
      parentEmail: "",
      privacyAccepted: true
    });
    setHasAllergies(false);
    setHasMedications(false);
    setHasDelegates(false);
    setAllergies([]);
    setMedications([]);
    setDelegates([]);
    setShowSuccessCard(false);
  };

  if (showSuccessCard && lastSubmittedStudent) {
    return (
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow-sm border border-slate-200 p-8 text-center">
        <div className="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
          <CheckCircle2 className="w-10 h-10" />
        </div>
        <h2 className="text-2xl font-bold text-slate-800 mb-2">Fascicolo Registrato Correttamente!</h2>
        <p className="text-slate-600 mb-6 text-sm">
          La scheda per lo studente <strong>{lastSubmittedStudent.firstName} {lastSubmittedStudent.lastName}</strong> è stata trasmessa alla segreteria e resa visibile al corpo docenti dell'I.C. Anzio 1.
        </p>

        <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 text-left text-xs text-slate-700 mb-6 space-y-2 max-w-lg mx-auto">
          <div className="flex justify-between pb-2 border-b border-slate-200">
            <span><strong>Plesso & Classe:</strong> {lastSubmittedStudent.campus} - {lastSubmittedStudent.classRoom}</span>
            <span><strong>Genitore:</strong> {lastSubmittedStudent.parentName}</span>
          </div>

          <div className="flex items-center gap-2 pt-1">
            <span className="font-semibold">Quadro Sanitario:</span>
            {lastSubmittedStudent.allergies.length > 0 ? (
              <span className="bg-amber-100 text-amber-900 px-2 py-0.5 rounded font-medium">
                {lastSubmittedStudent.allergies.length} allergia/e registrata/e
              </span>
            ) : (
              <span className="bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-medium">
                Nessuna allergia segnalata
              </span>
            )}
          </div>

          <div className="flex items-center gap-2">
            <span className="font-semibold">Farmaci a Scuola:</span>
            {lastSubmittedStudent.medications.length > 0 ? (
              <span className="bg-indigo-100 text-indigo-900 px-2 py-0.5 rounded font-medium">
                {lastSubmittedStudent.medications.length} farmaco/i in somministrazione
              </span>
            ) : (
              <span className="text-slate-500">Nessun farmaco necessario</span>
            )}
          </div>

          <div className="flex items-center gap-2">
            <span className="font-semibold">Deleghe di Uscita:</span>
            {lastSubmittedStudent.delegates.length > 0 ? (
              <span className="bg-blue-100 text-blue-900 px-2 py-0.5 rounded font-medium">
                {lastSubmittedStudent.delegates.length} persona/e delegata/e al ritiro
              </span>
            ) : (
              <span className="text-slate-500">Solo i genitori autorizzati al ritiro</span>
            )}
          </div>
        </div>

        <button
          onClick={resetForm}
          className="px-6 py-2.5 bg-blue-900 hover:bg-blue-800 text-white rounded-xl font-medium text-sm transition-colors shadow"
        >
          Compila nuova scheda o inserisci altro figlio
        </button>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Intro Banner */}
      <div className="bg-gradient-to-r from-blue-900 to-indigo-900 text-white rounded-2xl p-6 shadow-sm border border-blue-800">
        <div className="flex items-start gap-4">
          <div className="p-3 bg-white/10 rounded-xl">
            <HeartPulse className="w-7 h-7 text-amber-300" />
          </div>
          <div>
            <h2 className="text-xl font-bold">Portale Famiglie - Anno Scolastico 2026/2027</h2>
            <p className="text-sm text-blue-100 mt-1">
              Inserisci i dati essenziali dello studente. <strong>Le sezioni relative ad Allergie, Farmaci e Deleghe sono del tutto facoltative</strong>: compila solo quelle che riguardano la tua situazione (es. solo deleghe se non ci sono allergie, o viceversa).
            </p>
          </div>
        </div>
      </div>

      {validationError && (
        <div className="bg-red-50 border border-red-300 text-red-800 p-4 rounded-xl flex items-center gap-3 text-sm">
          <AlertCircle className="w-5 h-5 flex-shrink-0 text-red-600" />
          <span>{validationError}</span>
        </div>
      )}

      <form onSubmit={handleSubmit} className="space-y-6">
        
        {/* SEZIONE 1: Dati Obbligatori Alunno & Genitore */}
        <div className="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
          <div className="flex items-center gap-2.5 pb-4 mb-4 border-b border-slate-100 text-blue-950 font-bold">
            <School className="w-5 h-5 text-blue-700" />
            <h3 className="text-base sm:text-lg">1. Dati Essenziali Studente e Genitore <span className="text-xs text-red-600 font-normal">(* obbligatori)</span></h3>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Nome Alunno/a *
              </label>
              <input
                type="text"
                required
                placeholder="es. Leonardo"
                value={formData.firstName}
                onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
                className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Cognome Alunno/a *
              </label>
              <input
                type="text"
                required
                placeholder="es. Rossi"
                value={formData.lastName}
                onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
                className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Data di Nascita <span className="text-slate-400 font-normal">(facoltativa)</span>
              </label>
              <input
                type="date"
                value={formData.birthDate}
                onChange={(e) => setFormData({ ...formData, birthDate: e.target.value })}
                className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
              />
            </div>

            <div className="sm:col-span-2">
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Plesso Scolastico *
              </label>
              <select
                value={formData.campus}
                onChange={(e) => setFormData({ ...formData, campus: e.target.value })}
                className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white"
              >
                {campuses.map(c => <option key={c} value={c}>{c}</option>)}
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Classe / Sezione *
              </label>
              <select
                value={formData.classRoom}
                onChange={(e) => setFormData({ ...formData, classRoom: e.target.value })}
                className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 bg-white font-medium"
              >
                {classes.map(cl => <option key={cl} value={cl}>{cl}</option>)}
              </select>
            </div>
          </div>

          <div className="mt-5 pt-4 border-t border-slate-100">
            <h4 className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3">
              Recapito Telefonico Principale
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Nome e Cognome Genitore/Tutore *
                </label>
                <input
                  type="text"
                  required
                  placeholder="es. Mario Rossi (Padre)"
                  value={formData.parentName}
                  onChange={(e) => setFormData({ ...formData, parentName: e.target.value })}
                  className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Telefono Principale Reperibile *
                </label>
                <input
                  type="tel"
                  required
                  placeholder="es. +39 340 1234567"
                  value={formData.parentPhone}
                  onChange={(e) => setFormData({ ...formData, parentPhone: e.target.value })}
                  className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Email (Facoltativa)
                </label>
                <input
                  type="email"
                  placeholder="es. genitore@email.it"
                  value={formData.parentEmail}
                  onChange={(e) => setFormData({ ...formData, parentEmail: e.target.value })}
                  className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
                />
              </div>
            </div>
          </div>
        </div>

        {/* SEZIONE 2: Allergie e Intolleranze (FACOLTATIVA CON SWITCH) */}
        <div className={`rounded-2xl border transition-all p-6 ${hasAllergies ? 'bg-white border-amber-300 shadow-sm' : 'bg-slate-50/70 border-slate-200'}`}>
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200">
            <div className="flex items-center gap-2.5">
              <AlertTriangle className={`w-5 h-5 ${hasAllergies ? 'text-amber-500' : 'text-slate-400'}`} />
              <div>
                <h3 className="text-base sm:text-lg font-bold text-slate-900">
                  2. Allergie o Intolleranze Alimentari/Respiratorie
                </h3>
                <p className="text-xs text-slate-500">
                  {hasAllergies ? "Sezione abilitata: inserisci gli allergeni noti" : "Facoltativo: lascia disattivato se l'alunno non ha allergie"}
                </p>
              </div>
            </div>

            <button
              type="button"
              onClick={() => setHasAllergies(!hasAllergies)}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                hasAllergies
                  ? "bg-amber-500 text-white shadow-sm"
                  : "bg-white border border-slate-300 text-slate-700 hover:bg-slate-100"
              }`}
            >
              {hasAllergies ? <ToggleRight className="w-5 h-5" /> : <ToggleLeft className="w-5 h-5 text-slate-400" />}
              <span>{hasAllergies ? "Sì, ha allergie" : "Nessuna allergia"}</span>
            </button>
          </div>

          {hasAllergies ? (
            <div className="mt-4 space-y-4">
              {/* Existing Allergies list */}
              {allergies.length > 0 && (
                <div className="space-y-2">
                  {allergies.map(alg => (
                    <div
                      key={alg.id}
                      className={`p-3 rounded-xl border flex flex-col sm:flex-row sm:items-center justify-between gap-2 ${
                        alg.severity === "grave"
                          ? "bg-red-50 border-red-200"
                          : "bg-amber-50 border-amber-200"
                      }`}
                    >
                      <div className="space-y-0.5">
                        <div className="flex items-center gap-2">
                          <span className={`text-[10px] font-bold uppercase px-2 py-0.5 rounded ${
                            alg.severity === "grave" ? "bg-red-600 text-white" : "bg-amber-500 text-white"
                          }`}>
                            {alg.severity}
                          </span>
                          <span className="text-xs text-slate-500">[{alg.type}]</span>
                          <strong className="text-sm text-slate-900">{alg.substance}</strong>
                        </div>
                        {alg.emergencyPlan && (
                          <p className="text-xs text-slate-600">
                            <strong>Piano:</strong> {alg.emergencyPlan}
                          </p>
                        )}
                      </div>
                      <button
                        type="button"
                        onClick={() => handleRemoveAllergy(alg.id)}
                        className="text-xs text-red-600 hover:text-red-800 p-1 flex items-center gap-1 self-end sm:self-center"
                      >
                        <Trash2 className="w-4 h-4" /> Elimina
                      </button>
                    </div>
                  ))}
                </div>
              )}

              {/* Add Allergy Box */}
              <div className="bg-amber-50/40 p-4 rounded-xl border border-amber-200 space-y-3">
                <span className="text-xs font-bold text-slate-700 flex items-center gap-1">
                  <Plus className="w-4 h-4 text-amber-600" /> Aggiungi sostanza o allergene
                </span>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Tipologia</label>
                    <select
                      value={currentAllergy.type}
                      onChange={(e) => setCurrentAllergy({ ...currentAllergy, type: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    >
                      <option value="Alimentare">Alimentare (Mensa / Snack)</option>
                      <option value="Respiratoria">Respiratoria / Pollini</option>
                      <option value="Insetti / Veleno">Puntura api / vespe</option>
                      <option value="Farmacologica">Farmacologica</option>
                      <option value="Altro">Altro</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Allergene / Sostanza</label>
                    <input
                      type="text"
                      placeholder="es. Arachidi, Uova, Lattosio"
                      value={currentAllergy.substance}
                      onChange={(e) => setCurrentAllergy({ ...currentAllergy, substance: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Gravità</label>
                    <select
                      value={currentAllergy.severity}
                      onChange={(e) => setCurrentAllergy({ ...currentAllergy, severity: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    >
                      <option value="lieve">Lieve</option>
                      <option value="moderata">Moderata (disturbi gastro/cutanei)</option>
                      <option value="grave">Grave (Rischio anafilassi)</option>
                    </select>
                  </div>

                  <div className="sm:col-span-3">
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">
                      Istruzioni per docenti / Mensa in caso di contatto
                    </label>
                    <input
                      type="text"
                      placeholder="es. Dieta in mensa senza latticini; in caso di ingestione chiamare 118..."
                      value={currentAllergy.emergencyPlan}
                      onChange={(e) => setCurrentAllergy({ ...currentAllergy, emergencyPlan: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>
                </div>

                <div className="text-right">
                  <button
                    type="button"
                    onClick={handleAddAllergy}
                    className="px-3 py-1.5 bg-amber-600 hover:bg-amber-700 text-white rounded-lg text-xs font-semibold transition-colors inline-flex items-center gap-1"
                  >
                    <Plus className="w-3.5 h-3.5" /> Salva allergia nell'elenco
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="mt-3 text-xs text-slate-500 italic bg-white p-3 rounded-lg border border-slate-200 flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-600" />
              <span>Nessuna allergia segnalata. L'alunno potrà seguire la dieta ordinaria della mensa scolastica.</span>
            </div>
          )}
        </div>

        {/* SEZIONE 3: Farmaci e Terapie a Scuola (FACOLTATIVA CON SWITCH) */}
        <div className={`rounded-2xl border transition-all p-6 ${hasMedications ? 'bg-white border-indigo-300 shadow-sm' : 'bg-slate-50/70 border-slate-200'}`}>
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200">
            <div className="flex items-center gap-2.5">
              <Pill className={`w-5 h-5 ${hasMedications ? 'text-indigo-600' : 'text-slate-400'}`} />
              <div>
                <h3 className="text-base sm:text-lg font-bold text-slate-900">
                  3. Somministrazione Farmaci o Terapie a Scuola
                </h3>
                <p className="text-xs text-slate-500">
                  {hasMedications ? "Sezione abilitata: indica il medicinale e le dosi" : "Facoltativo: lascia disattivato se l'alunno non deve assumere farmaci a scuola"}
                </p>
              </div>
            </div>

            <button
              type="button"
              onClick={() => setHasMedications(!hasMedications)}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                hasMedications
                  ? "bg-indigo-600 text-white shadow-sm"
                  : "bg-white border border-slate-300 text-slate-700 hover:bg-slate-100"
              }`}
            >
              {hasMedications ? <ToggleRight className="w-5 h-5" /> : <ToggleLeft className="w-5 h-5 text-slate-400" />}
              <span>{hasMedications ? "Sì, necessita farmaci" : "Nessun farmaco"}</span>
            </button>
          </div>

          {hasMedications ? (
            <div className="mt-4 space-y-4">
              {medications.length > 0 && (
                <div className="space-y-2">
                  {medications.map(med => (
                    <div
                      key={med.id}
                      className="p-3 rounded-xl border border-indigo-100 bg-indigo-50/60 flex flex-col sm:flex-row sm:items-center justify-between gap-2"
                    >
                      <div className="space-y-0.5">
                        <div className="flex items-center gap-2">
                          <strong className="text-sm text-indigo-950 font-bold">{med.name}</strong>
                          <span className="text-xs bg-indigo-200 text-indigo-900 px-2 py-0.5 rounded font-mono">
                            {med.dosage}
                          </span>
                          <span className="text-xs text-slate-600 flex items-center gap-1">
                            <Clock className="w-3 h-3 text-indigo-500" /> {med.timing}
                          </span>
                        </div>
                        {med.notes && <p className="text-xs text-slate-600">Note: {med.notes}</p>}
                      </div>
                      <button
                        type="button"
                        onClick={() => handleRemoveMedication(med.id)}
                        className="text-xs text-red-600 hover:text-red-800 p-1 flex items-center gap-1 self-end sm:self-center"
                      >
                        <Trash2 className="w-4 h-4" /> Elimina
                      </button>
                    </div>
                  ))}
                </div>
              )}

              {/* Add Med box */}
              <div className="bg-indigo-50/30 p-4 rounded-xl border border-indigo-200 space-y-3">
                <span className="text-xs font-bold text-slate-700 flex items-center gap-1">
                  <Plus className="w-4 h-4 text-indigo-600" /> Inserisci farmaco prescritto
                </span>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Nome Farmaco</label>
                    <input
                      type="text"
                      placeholder="es. Ventolin, Bentelan"
                      value={currentMed.name}
                      onChange={(e) => setCurrentMed({ ...currentMed, name: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Dosaggio</label>
                    <input
                      type="text"
                      placeholder="es. 2 spruzzi, 1 bustina"
                      value={currentMed.dosage}
                      onChange={(e) => setCurrentMed({ ...currentMed, dosage: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Orario o Modalità</label>
                    <input
                      type="text"
                      placeholder="es. Ore 12:30 o al bisogno"
                      value={currentMed.timing}
                      onChange={(e) => setCurrentMed({ ...currentMed, timing: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>

                  <div className="sm:col-span-3">
                    <label className="block text-[11px] font-semibold text-slate-600 mb-1">Note e custodia a scuola</label>
                    <input
                      type="text"
                      placeholder="es. Custodito nel cassetto farmaci del plesso con prescrizione medica..."
                      value={currentMed.notes}
                      onChange={(e) => setCurrentMed({ ...currentMed, notes: e.target.value })}
                      className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                    />
                  </div>
                </div>

                <div className="text-right">
                  <button
                    type="button"
                    onClick={handleAddMedication}
                    className="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-semibold transition-colors inline-flex items-center gap-1"
                  >
                    <Plus className="w-3.5 h-3.5" /> Salva farmaco
                  </button>
                </div>
              </div>
            </div>
          ) : (
            <div className="mt-3 text-xs text-slate-500 italic bg-white p-3 rounded-lg border border-slate-200 flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-600" />
              <span>Nessun farmaco richiesto. Nessuna somministrazione prevista in orario scolastico.</span>
            </div>
          )}
        </div>

        {/* SEZIONE 4: Deleghe di Uscita (FACOLTATIVA CON SWITCH) */}
        <div className={`rounded-2xl border transition-all p-6 ${hasDelegates ? 'bg-white border-emerald-300 shadow-sm' : 'bg-slate-50/70 border-slate-200'}`}>
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200">
            <div className="flex items-center gap-2.5">
              <UserCheck className={`w-5 h-5 ${hasDelegates ? 'text-emerald-600' : 'text-slate-400'}`} />
              <div>
                <h3 className="text-base sm:text-lg font-bold text-slate-900">
                  4. Deleghe di Uscita e Ritiro Studente
                </h3>
                <p className="text-xs text-slate-500">
                  {hasDelegates ? "Sezione abilitata: registra le persone autorizzate con documento d'identità" : "Facoltativo: lascia disattivato se ritirano sempre e solo i genitori"}
                </p>
              </div>
            </div>

            <button
              type="button"
              onClick={() => handleToggleDelegates(!hasDelegates)}
              className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-2 ${
                hasDelegates
                  ? "bg-emerald-600 text-white shadow-sm"
                  : "bg-white border border-slate-300 text-slate-700 hover:bg-slate-100"
              }`}
            >
              {hasDelegates ? <ToggleRight className="w-5 h-5" /> : <ToggleLeft className="w-5 h-5 text-slate-400" />}
              <span>{hasDelegates ? "Delego persone al ritiro" : "Nessuna delega (solo genitori)"}</span>
            </button>
          </div>

          {hasDelegates ? (
            <div className="mt-4 space-y-4">
              <div className="flex items-center justify-between">
                <span className="text-xs text-slate-600">
                  Inserisci le persone maggiorenni autorizzate. Per ciascuna è richiesta la Carta d'Identità per il controllo a scuola.
                </span>
                <button
                  type="button"
                  onClick={handleAddDelegate}
                  className="text-xs bg-emerald-50 hover:bg-emerald-100 text-emerald-800 font-semibold px-2.5 py-1.5 rounded-lg border border-emerald-300 transition-colors flex items-center gap-1"
                >
                  <Plus className="w-3.5 h-3.5" /> Altro delegato
                </button>
              </div>

              {delegates.map((del, idx) => (
                <div key={del.id} className="p-4 rounded-xl border border-slate-200 bg-slate-50/50 space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                      <span className="w-5 h-5 rounded-full bg-slate-700 text-white flex items-center justify-center text-[10px]">
                        {idx + 1}
                      </span>
                      Delegato al Ritiro
                    </span>
                    <button
                      type="button"
                      onClick={() => handleRemoveDelegate(del.id)}
                      className="text-xs text-red-600 hover:text-red-800 flex items-center gap-1"
                    >
                      <Trash2 className="w-3.5 h-3.5" /> Rimuovi
                    </button>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Nome Delegato *</label>
                      <input
                        type="text"
                        required
                        placeholder="es. Nonna Maria"
                        value={del.firstName}
                        onChange={(e) => handleDelegateChange(del.id, 'firstName', e.target.value)}
                        className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                      />
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Cognome Delegato *</label>
                      <input
                        type="text"
                        required
                        placeholder="es. Bianchi"
                        value={del.lastName}
                        onChange={(e) => handleDelegateChange(del.id, 'lastName', e.target.value)}
                        className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                      />
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Grado di Parentela</label>
                      <input
                        type="text"
                        placeholder="es. Nonna materna, Zio, Amico"
                        value={del.relationship}
                        onChange={(e) => handleDelegateChange(del.id, 'relationship', e.target.value)}
                        className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                      />
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">
                        Numero Carta d'Identità *
                      </label>
                      <div className="relative">
                        <IdCard className="w-3.5 h-3.5 absolute left-2.5 top-2.5 text-slate-400" />
                        <input
                          type="text"
                          required
                          placeholder="es. CA98765ZX"
                          value={del.idCardNumber}
                          onChange={(e) => handleDelegateChange(del.id, 'idCardNumber', e.target.value.toUpperCase())}
                          className="w-full pl-8 pr-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white font-mono uppercase font-bold"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Telefono Delegato</label>
                      <input
                        type="tel"
                        placeholder="es. +39 333 1234567"
                        value={del.phone}
                        onChange={(e) => handleDelegateChange(del.id, 'phone', e.target.value)}
                        className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                      />
                    </div>

                    <div>
                      <label className="block text-[11px] font-semibold text-slate-600 mb-1">Note / Frequenza ritiro</label>
                      <input
                        type="text"
                        placeholder="es. Tutti i giorni, oppure solo mercoledì"
                        value={del.note}
                        onChange={(e) => handleDelegateChange(del.id, 'note', e.target.value)}
                        className="w-full px-2.5 py-1.5 text-xs rounded-lg border border-slate-300 bg-white"
                      />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="mt-3 text-xs text-slate-500 italic bg-white p-3 rounded-lg border border-slate-200 flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-600" />
              <span>Nessuna delega esterna: l'alunno potrà essere prelevato al termine delle lezioni unicamente dai genitori o tutori legali.</span>
            </div>
          )}
        </div>

        {/* SEZIONE 5: Privacy e Invio */}
        <div className="bg-white rounded-2xl border border-blue-200 p-6 shadow-sm space-y-4">
          <div className="flex items-center gap-2 text-blue-950 font-bold">
            <Shield className="w-5 h-5 text-blue-700" />
            <h3 className="text-base sm:text-lg">5. Conferma e Trasmissione Fascicolo</h3>
          </div>

          <label className="flex items-start gap-3 cursor-pointer">
            <input
              type="checkbox"
              required
              checked={formData.privacyAccepted}
              onChange={(e) => setFormData({ ...formData, privacyAccepted: e.target.checked })}
              className="mt-1 w-4 h-4 rounded text-blue-900 border-slate-300 focus:ring-blue-600"
            />
            <span className="text-xs text-slate-700">
              Confermo la veridicità delle informazioni inserite e autorizzo l'I.C. Anzio 1 al trattamento dei dati anagrafici, sanitari e di delega secondo il GDPR UE 2016/679 per fini istituzionali di sicurezza scolastica. *
            </span>
          </label>

          <div className="pt-4 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="text-xs text-slate-500 flex items-center gap-1.5">
              <Lock className="w-3.5 h-3.5 text-emerald-600" />
              <span>Trasmissione sicura al Registro Riservato I.C. Anzio 1</span>
            </div>

            <button
              type="submit"
              className="w-full sm:w-auto px-8 py-3 bg-gradient-to-r from-blue-900 to-indigo-900 hover:from-blue-800 hover:to-indigo-800 text-white font-semibold rounded-xl shadow-md transition-all flex items-center justify-center gap-2"
            >
              <CheckCircle2 className="w-4 h-4" />
              Invia Fascicolo alla Scuola
            </button>
          </div>
        </div>

      </form>
    </div>
  );
}

/* =========================================================================
   TEACHER DASHBOARD VIEW (Consultazione con Badge e Filtri Intelligenti)
   ========================================================================= */
function TeacherDashboardView({
  teacherAuth,
  students,
  allStudents,
  searchTerm,
  setSearchTerm,
  selectedClass,
  setSelectedClass,
  selectedCampus,
  setSelectedCampus,
  filterType,
  setFilterType,
  campuses,
  classes,
  onOpenStudentDetail,
  isPickupQuickMode,
  setIsPickupQuickMode
}) {
  const totalStudents = allStudents.length;
  const severeCount = allStudents.filter(s => s.allergies.some(a => a.severity === 'grave')).length;
  const onlyDelegatesCount = allStudents.filter(s => s.delegates.length > 0 && s.allergies.length === 0 && s.medications.length === 0).length;

  return (
    <div className="space-y-6">
      {/* Top Header */}
      <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-100 text-emerald-800 uppercase tracking-wide">
              Docente In Servizio
            </span>
            <span className="text-xs text-slate-500 font-mono">ID: {teacherAuth.teacherCode}</span>
          </div>
          <h2 className="text-xl font-bold text-slate-900 mt-1">
            Registro Salute, Terapie e Deleghe di Uscita
          </h2>
          <p className="text-xs text-slate-500">
            Istituto Comprensivo Anzio 1 • Accesso riservato al personale in servizio
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2.5">
          <button
            onClick={() => setIsPickupQuickMode(!isPickupQuickMode)}
            className={`px-3.5 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center gap-2 border ${
              isPickupQuickMode
                ? "bg-amber-500 text-white border-amber-600 shadow-sm"
                : "bg-slate-100 text-slate-700 hover:bg-slate-200 border-slate-300"
            }`}
          >
            <UserCheck className="w-4 h-4" />
            {isPickupQuickMode ? "Modalità Standard" : "Modalità Campanella / Controllo Rapido Deleghe"}
          </button>

          <button
            onClick={() => window.print()}
            className="px-3.5 py-2 bg-blue-900 hover:bg-blue-800 text-white rounded-xl text-xs sm:text-sm font-medium transition-all shadow-sm flex items-center gap-2"
          >
            <Printer className="w-4 h-4" />
            <span className="hidden sm:inline">Stampa Fascicolo Classe</span>
          </button>
        </div>
      </div>

      {/* KPI Counters */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm flex items-center gap-3">
          <div className="p-3 bg-blue-50 text-blue-700 rounded-xl">
            <Users className="w-6 h-6" />
          </div>
          <div>
            <div className="text-2xl font-bold text-slate-800">{totalStudents}</div>
            <div className="text-xs text-slate-500">Fascicoli Alunni Totali</div>
          </div>
        </div>

        <div className="bg-white p-4 rounded-xl border border-red-200 shadow-sm flex items-center gap-3">
          <div className="p-3 bg-red-50 text-red-600 rounded-xl">
            <AlertTriangle className="w-6 h-6" />
          </div>
          <div>
            <div className="text-2xl font-bold text-red-700">{severeCount}</div>
            <div className="text-xs text-red-800 font-medium">Allergie Gravi (Rischio Shock)</div>
          </div>
        </div>

        <div className="bg-white p-4 rounded-xl border border-emerald-200 shadow-sm flex items-center gap-3">
          <div className="p-3 bg-emerald-50 text-emerald-700 rounded-xl">
            <UserCheck className="w-6 h-6" />
          </div>
          <div>
            <div className="text-2xl font-bold text-emerald-800">{onlyDelegatesCount}</div>
            <div className="text-xs text-slate-500">Solo Deleghe (Nessuna Allergia)</div>
          </div>
        </div>
      </div>

      {/* Filters Bar */}
      <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-3">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-3 text-slate-400" />
            <input
              type="text"
              placeholder="Cerca alunno, delegato, carta identità..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-9 pr-3 py-2 text-xs rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />
          </div>

          <div>
            <select
              value={selectedClass}
              onChange={(e) => setSelectedClass(e.target.value)}
              className="w-full px-3 py-2 text-xs rounded-xl border border-slate-300 bg-white"
            >
              <option value="all">Tutte le Classi</option>
              {classes.map(cl => <option key={cl} value={cl}>Classe {cl}</option>)}
            </select>
          </div>

          <div>
            <select
              value={selectedCampus}
              onChange={(e) => setSelectedCampus(e.target.value)}
              className="w-full px-3 py-2 text-xs rounded-xl border border-slate-300 bg-white"
            >
              <option value="all">Tutti i Plessi</option>
              {campuses.map(cp => <option key={cp} value={cp}>{cp}</option>)}
            </select>
          </div>

          <div>
            <select
              value={filterType}
              onChange={(e) => setFilterType(e.target.value)}
              className="w-full px-3 py-2 text-xs rounded-xl border border-slate-300 bg-white font-medium"
            >
              <option value="all">Mostra Tutti gli Alunni</option>
              <option value="only_delegates">Solo con Deleghe (Senza Allergie)</option>
              <option value="severe">Solo con Allergie Gravi</option>
              <option value="allergies">Tutti con Allergie / Diete</option>
              <option value="meds">Con Terapie / Farmaci</option>
              <option value="no_allergies">Nessuna Allergia</option>
            </select>
          </div>
        </div>
      </div>

      {/* QUICK PICKUP / BELL TIME MODE */}
      {isPickupQuickMode ? (
        <QuickPickupView
          students={students}
          onOpenStudentDetail={onOpenStudentDetail}
        />
      ) : (
        /* STANDARD LIST VIEW */
        <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
          <div className="px-5 py-3.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between">
            <span className="text-xs font-bold text-slate-700 uppercase tracking-wider">
              Elenco Fascicoli Studenti ({students.length} Trovati)
            </span>
            <span className="text-[11px] text-slate-500">
              Clicca per visualizzare la scheda dettagliata
            </span>
          </div>

          {students.length === 0 ? (
            <div className="p-12 text-center text-slate-500">
              <Users className="w-12 h-12 text-slate-300 mx-auto mb-2" />
              <p className="font-semibold text-sm">Nessun alunno trovato per questa selezione.</p>
            </div>
          ) : (
            <div className="divide-y divide-slate-100">
              {students.map((student) => {
                const hasSevere = student.allergies.some(a => a.severity === 'grave');
                const hasMeds = student.medications.length > 0;
                const hasAllergies = student.allergies.length > 0;
                const hasDelegates = student.delegates.length > 0;
                const isOnlyDelegates = hasDelegates && !hasAllergies && !hasMeds;

                return (
                  <div
                    key={student.id}
                    onClick={() => onOpenStudentDetail(student)}
                    className="p-4 sm:p-5 hover:bg-blue-50/40 transition-colors cursor-pointer flex flex-col md:flex-row md:items-center justify-between gap-4"
                  >
                    <div className="flex items-start gap-3.5">
                      <div className="w-10 h-10 rounded-xl bg-blue-100 text-blue-900 font-bold flex items-center justify-center flex-shrink-0 text-sm">
                        {student.firstName[0]}{student.lastName[0]}
                      </div>
                      <div>
                        <div className="flex items-center gap-2">
                          <h4 className="font-bold text-slate-900 text-base">
                            {student.lastName} {student.firstName}
                          </h4>
                          <span className="px-2 py-0.5 rounded bg-blue-900 text-white text-xs font-semibold">
                            {student.classRoom}
                          </span>
                        </div>
                        <p className="text-xs text-slate-500">
                          {student.campus} • Genitore: {student.parentName} ({student.parentPhone})
                        </p>
                      </div>
                    </div>

                    {/* Dynamic Status Badges */}
                    <div className="flex flex-wrap items-center gap-2">
                      {isOnlyDelegates && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-50 text-emerald-800 border border-emerald-200">
                          <Check className="w-3.5 h-3.5 text-emerald-600" />
                          Solo Deleghe ({student.delegates.length})
                        </span>
                      )}

                      {hasSevere && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold bg-red-100 text-red-800 border border-red-200">
                          <AlertTriangle className="w-3.5 h-3.5 text-red-600" />
                          Allergia Grave
                        </span>
                      )}

                      {hasAllergies && !hasSevere && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-100 text-amber-800 border border-amber-200">
                          {student.allergies.length} Allergia/e
                        </span>
                      )}

                      {!hasAllergies && !isOnlyDelegates && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-normal bg-slate-100 text-slate-600 border border-slate-200">
                          Nessuna Allergia
                        </span>
                      )}

                      {hasMeds && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-800 border border-indigo-200">
                          <Pill className="w-3.5 h-3.5 text-indigo-600" />
                          {student.medications.length} Farmaco/i
                        </span>
                      )}

                      {!isOnlyDelegates && (
                        <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-700 border border-slate-200">
                          <UserCheck className="w-3.5 h-3.5 text-emerald-600" />
                          {student.delegates.length > 0 ? `${student.delegates.length} Delegati` : "Solo Genitori"}
                        </span>
                      )}

                      <div className="text-blue-700 hover:text-blue-900 pl-2">
                        <ChevronRight className="w-5 h-5" />
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* Print Table for School Staff */}
      <div className="hidden print:block print:p-4 text-slate-900 bg-white">
        <div className="border-b-2 border-black pb-3 mb-4 flex justify-between items-center">
          <div>
            <h1 className="text-xl font-bold uppercase">Istituto Comprensivo Anzio 1</h1>
            <h2 className="text-sm font-semibold">Registro Riservato Sanitario & Deleghe Uscita</h2>
          </div>
          <div className="text-right text-xs">
            <p>Data Stampa: {new Date().toLocaleDateString('it-IT')}</p>
            <p className="font-bold text-red-600">STRETTAMENTE RISERVATO - D.LGS 196/2003</p>
          </div>
        </div>

        <table className="w-full text-xs border-collapse border border-slate-400">
          <thead>
            <tr className="bg-slate-100 text-left">
              <th className="border border-slate-300 p-2">Alunno / Plesso</th>
              <th className="border border-slate-300 p-2">Allergie & Protocolli</th>
              <th className="border border-slate-300 p-2">Farmaci</th>
              <th className="border border-slate-300 p-2">Deleghe Uscita (Doc. Identità)</th>
            </tr>
          </thead>
          <tbody>
            {students.map(s => (
              <tr key={s.id} className="align-top">
                <td className="border border-slate-300 p-2 font-bold">
                  {s.lastName} {s.firstName} ({s.classRoom})<br />
                  <span className="font-normal text-[10px] text-slate-600">{s.campus}</span>
                </td>
                <td className="border border-slate-300 p-2">
                  {s.allergies.length === 0 ? "Nessuna allergia" : (
                    s.allergies.map(a => (
                      <div key={a.id} className="mb-1">
                        <strong>{a.substance}</strong> ({a.severity})
                        {a.emergencyPlan && <div className="text-[10px] italic">{a.emergencyPlan}</div>}
                      </div>
                    ))
                  )}
                </td>
                <td className="border border-slate-300 p-2">
                  {s.medications.length === 0 ? "Nessun farmaco" : (
                    s.medications.map(m => (
                      <div key={m.id} className="mb-1">
                        <strong>{m.name}</strong> ({m.dosage} - {m.timing})
                      </div>
                    ))
                  )}
                </td>
                <td className="border border-slate-300 p-2">
                  {s.delegates.length === 0 ? "Solo genitori" : (
                    s.delegates.map(d => (
                      <div key={d.id} className="text-[11px] mb-1">
                        <strong>{d.lastName} {d.firstName}</strong> ({d.relationship})
                        <br />Doc: <span className="font-mono">{d.idCardNumber}</span> | Tel: {d.phone}
                      </div>
                    ))
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

/* =========================================================================
   QUICK PICKUP MODE & MODAL (Invariati con compatibilità per liste vuote)
   ========================================================================= */
function QuickPickupView({ students, onOpenStudentDetail }) {
  const [filterQuery, setFilterQuery] = useState("");

  const matchingStudents = students.filter(s =>
    `${s.firstName} ${s.lastName}`.toLowerCase().includes(filterQuery.toLowerCase()) ||
    s.delegates.some(d =>
      `${d.firstName} ${d.lastName}`.toLowerCase().includes(filterQuery.toLowerCase()) ||
      d.idCardNumber.toLowerCase().includes(filterQuery.toLowerCase())
    )
  );

  return (
    <div className="bg-amber-50/70 border-2 border-amber-300 rounded-2xl p-5 shadow-sm space-y-4">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-amber-200">
        <div className="flex items-center gap-2.5">
          <div className="p-2 rounded-xl bg-amber-400 text-slate-900">
            <Clock className="w-6 h-6" />
          </div>
          <div>
            <h3 className="font-bold text-slate-900 text-lg">
              Modalità Campanella: Controllo Documento Deleghe
            </h3>
            <p className="text-xs text-slate-600">
              Verifica rapida della Carta d'Identità dei delegati autorizzati al momento del ritiro.
            </p>
          </div>
        </div>

        <div className="w-full sm:w-72">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-3 text-amber-700" />
            <input
              type="text"
              autoFocus
              placeholder="Cerca nome delegato o Carta Identità..."
              value={filterQuery}
              onChange={(e) => setFilterQuery(e.target.value)}
              className="w-full pl-9 pr-3 py-2 text-xs rounded-xl border border-amber-400 bg-white focus:outline-none focus:ring-2 focus:ring-amber-500 font-medium"
            />
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {matchingStudents.map((st) => (
          <div
            key={st.id}
            className="bg-white rounded-xl border border-amber-200 p-4 shadow-sm hover:border-amber-400 transition-colors"
          >
            <div className="flex items-center justify-between mb-2">
              <span className="font-bold text-slate-900 text-sm">
                Alunno: {st.lastName} {st.firstName}
              </span>
              <span className="px-2 py-0.5 rounded bg-blue-900 text-white text-xs font-bold">
                {st.classRoom}
              </span>
            </div>

            <p className="text-xs text-slate-500 mb-3">{st.campus}</p>

            <div className="space-y-2">
              <span className="text-[11px] font-semibold text-slate-600 uppercase tracking-wide">
                Persone autorizzate al ritiro:
              </span>
              {st.delegates.length === 0 ? (
                <p className="text-xs text-slate-500 italic bg-slate-50 p-2 rounded">
                  Nessun delegato: solo i genitori ({st.parentName})
                </p>
              ) : (
                st.delegates.map(del => (
                  <div
                    key={del.id}
                    className="p-2.5 rounded-lg bg-slate-50 border border-slate-200 text-xs flex items-center justify-between"
                  >
                    <div>
                      <div className="font-bold text-slate-800 flex items-center gap-1.5">
                        <UserCheck className="w-3.5 h-3.5 text-emerald-600" />
                        {del.lastName} {del.firstName}
                        <span className="text-[11px] text-slate-500 font-normal">({del.relationship})</span>
                      </div>
                      <div className="text-[11px] text-slate-600 mt-0.5 flex items-center gap-2">
                        <span className="font-mono bg-amber-100 text-amber-950 px-1.5 py-0.5 rounded font-bold">
                          Doc: {del.idCardNumber}
                        </span>
                        {del.phone && <span>Tel: {del.phone}</span>}
                      </div>
                    </div>
                    <span className="text-[10px] text-emerald-700 bg-emerald-50 px-2 py-1 rounded font-semibold border border-emerald-200">
                      Abilitato
                    </span>
                  </div>
                ))
              )}
            </div>

            <div className="mt-3 pt-2 border-t border-slate-100 text-right">
              <button
                onClick={() => onOpenStudentDetail(st)}
                className="text-xs text-blue-700 hover:text-blue-900 font-semibold"
              >
                Vedi scheda completa →
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function StudentDetailModal({ student, onClose }) {
  if (!student) return null;
  const severeAllergies = student.allergies.filter(a => a.severity === 'grave');

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
      <div className="bg-white rounded-2xl shadow-2xl border border-slate-200 w-full max-w-2xl overflow-hidden my-6">
        
        <div className="bg-gradient-to-r from-blue-950 to-indigo-950 text-white p-5 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-400 text-blue-950 flex items-center justify-center font-bold text-base">
              {student.firstName[0]}{student.lastName[0]}
            </div>
            <div>
              <h3 className="text-lg font-bold">
                {student.lastName} {student.firstName}
              </h3>
              <p className="text-xs text-blue-200">
                Classe {student.classRoom} • {student.campus}
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors"
          >
            ✕
          </button>
        </div>

        <div className="p-6 space-y-6 max-h-[75vh] overflow-y-auto text-slate-800">
          {severeAllergies.length > 0 && (
            <div className="p-4 bg-red-50 border-2 border-red-300 rounded-xl flex items-start gap-3">
              <AlertTriangle className="w-6 h-6 text-red-600 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="text-sm font-bold text-red-900 uppercase tracking-wide">
                  Attenzione Primaria: Allergia ad Alto Rischio
                </h4>
                {severeAllergies.map(s => (
                  <div key={s.id} className="mt-1 text-xs text-red-800">
                    <p><strong>Allergene:</strong> {s.substance}</p>
                    <p><strong>Procedura Immediata:</strong> {s.emergencyPlan || "Contattare immediatamente il 118 e avvisare la famiglia."}</p>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs bg-slate-50 p-3.5 rounded-xl border border-slate-200">
            <div>
              <span className="text-slate-500 block">Genitore / Referente:</span>
              <strong className="text-slate-800 text-sm">{student.parentName}</strong>
            </div>
            <div>
              <span className="text-slate-500 block">Telefono Reperibile:</span>
              <strong className="text-slate-900 text-sm font-mono flex items-center gap-1">
                <Phone className="w-3.5 h-3.5 text-emerald-600" />
                {student.parentPhone}
              </strong>
            </div>
            <div>
              <span className="text-slate-500 block">Email registrata:</span>
              <span className="text-slate-700">{student.parentEmail}</span>
            </div>
            <div>
              <span className="text-slate-500 block">Ultimo Aggiornamento:</span>
              <span className="text-slate-700">{student.updatedAt}</span>
            </div>
          </div>

          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2 flex items-center gap-1.5">
              <AlertTriangle className="w-4 h-4 text-amber-500" /> Allergie & Intolleranze
            </h4>
            {student.allergies.length === 0 ? (
              <p className="text-xs text-slate-500 italic bg-emerald-50 text-emerald-800 p-3 rounded-lg border border-emerald-200 flex items-center gap-2">
                <Check className="w-4 h-4 text-emerald-600" /> Nessuna allergia segnalata dalla famiglia.
              </p>
            ) : (
              <div className="space-y-2">
                {student.allergies.map(alg => (
                  <div key={alg.id} className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-xs">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-slate-900">{alg.substance} ({alg.type})</span>
                      <span className={`px-2 py-0.5 rounded text-[10px] font-bold uppercase ${
                        alg.severity === 'grave' ? 'bg-red-600 text-white' : 'bg-amber-400 text-slate-900'
                      }`}>
                        {alg.severity}
                      </span>
                    </div>
                    {alg.emergencyPlan && (
                      <p className="text-slate-600 mt-1.5">
                        <strong>Piano d'intervento:</strong> {alg.emergencyPlan}
                      </p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>

          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2 flex items-center gap-1.5">
              <Pill className="w-4 h-4 text-indigo-600" /> Farmaci & Terapie a Scuola
            </h4>
            {student.medications.length === 0 ? (
              <p className="text-xs text-slate-500 italic bg-slate-50 p-3 rounded-lg border border-slate-200">
                Nessun farmaco autorizzato o depositato per questo alunno.
              </p>
            ) : (
              <div className="space-y-2">
                {student.medications.map(med => (
                  <div key={med.id} className="p-3 rounded-xl border border-indigo-100 bg-indigo-50/50 text-xs">
                    <div className="flex items-center justify-between">
                      <strong className="text-indigo-950 font-bold">{med.name}</strong>
                      <span className="font-mono bg-indigo-100 text-indigo-800 px-2 py-0.5 rounded">
                        {med.dosage}
                      </span>
                    </div>
                    <p className="text-slate-600 mt-1">
                      <strong>Orario:</strong> {med.timing}
                    </p>
                    {med.notes && (
                      <p className="text-slate-500 mt-0.5 italic">Note: {med.notes}</p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>

          <div>
            <h4 className="text-xs font-bold uppercase tracking-wider text-slate-500 mb-2 flex items-center gap-1.5">
              <UserCheck className="w-4 h-4 text-emerald-600" /> Soggetti Delegati al Ritiro
            </h4>
            {student.delegates.length === 0 ? (
              <p className="text-xs text-slate-500 italic bg-slate-50 p-3 rounded-lg border border-slate-200">
                Nessun delegato: autorizzati al ritiro esclusivamente i genitori o esercenti la responsabilità genitoriale.
              </p>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {student.delegates.map(del => (
                  <div key={del.id} className="p-3 rounded-xl border border-slate-200 bg-slate-50 text-xs">
                    <div className="font-bold text-slate-900">{del.lastName} {del.firstName}</div>
                    <div className="text-slate-500">{del.relationship}</div>
                    <div className="mt-2 pt-2 border-t border-slate-200 font-mono text-[11px] text-slate-700">
                      <strong>C.I.:</strong> {del.idCardNumber}
                    </div>
                    {del.phone && <div className="text-[11px] text-slate-600 mt-0.5">Tel: {del.phone}</div>}
                    {del.note && <div className="text-[10px] text-slate-500 italic mt-1">{del.note}</div>}
                  </div>
                ))}
              </div>
            )}
          </div>

        </div>

        <div className="p-4 bg-slate-50 border-t border-slate-200 flex justify-end">
          <button
            onClick={onClose}
            className="px-5 py-2 bg-slate-800 hover:bg-slate-700 text-white rounded-xl text-xs font-semibold transition-colors"
          >
            Chiudi Scheda
          </button>
        </div>

      </div>
    </div>
  );
}

function TeacherLoginView({
  loginPassword,
  setLoginPassword,
  loginCode,
  setLoginCode,
  loginError,
  onSubmit,
  onBackToParent
}) {
  return (
    <div className="max-w-md mx-auto py-8">
      <div className="bg-white rounded-2xl shadow-md border border-slate-200 overflow-hidden">
        <div className="bg-gradient-to-r from-blue-950 to-indigo-950 p-6 text-white text-center">
          <div className="w-14 h-14 rounded-2xl bg-amber-400 text-blue-950 flex items-center justify-center mx-auto mb-3 shadow">
            <Lock className="w-7 h-7" />
          </div>
          <h2 className="text-xl font-bold">Area Riservata Docenti e ATA</h2>
          <p className="text-xs text-blue-200 mt-1">
            Accesso protetto per la consultazione dei dati sanitari e deleghe autorizzate
          </p>
        </div>

        <form onSubmit={onSubmit} className="p-6 space-y-4">
          {loginError && (
            <div className="p-3 bg-red-50 border border-red-300 text-red-800 rounded-xl text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 flex-shrink-0 text-red-600" />
              <span>{loginError}</span>
            </div>
          )}

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Identificativo Docente (Opzionale)
            </label>
            <input
              type="text"
              placeholder="es. DOC-ANZIO1"
              value={loginCode}
              onChange={(e) => setLoginCode(e.target.value)}
              className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600 font-mono uppercase"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Password Istituzionale di Sicurezza *
            </label>
            <input
              type="password"
              required
              placeholder="Inserisci password docenti..."
              value={loginPassword}
              onChange={(e) => setLoginPassword(e.target.value)}
              className="w-full px-3 py-2 text-sm rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-600"
            />
          </div>

          <div className="bg-amber-50 border border-amber-200 rounded-xl p-3 text-xs text-amber-900 space-y-1">
            <p className="font-bold flex items-center gap-1 text-amber-800">
              <Info className="w-4 h-4 text-amber-600" /> Credenziali di Test Docenti:
            </p>
            <p>Password: <code className="bg-amber-200 font-mono font-bold px-1.5 py-0.5 rounded text-slate-900">Anzio1Docenti#</code> oppure <code className="bg-amber-200 font-mono font-bold px-1.5 py-0.5 rounded text-slate-900">Docente2026!</code></p>
          </div>

          <div className="pt-2">
            <button
              type="submit"
              className="w-full py-2.5 bg-blue-950 hover:bg-blue-900 text-white font-semibold rounded-xl text-sm transition-all shadow-md flex items-center justify-center gap-2"
            >
              <ShieldCheck className="w-4 h-4 text-amber-400" />
              Accedi alla Dashboard Riservata
            </button>
          </div>

          <div className="text-center pt-2">
            <button
              type="button"
              onClick={onBackToParent}
              className="text-xs text-slate-500 hover:text-slate-800 underline"
            >
              Torna al modulo famiglie
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
