# Software Requirement Specification (SRS)
## Project: Mental Health Sentiment Tracker (v1.0)

---

### 1. Introduction
#### 1.1 Purpose
The purpose of this document is to explicitly define the software requirements for the **Mental Health Sentiment Tracker**. This application functions as a local, privacy-first digital companion that analyzes text-based user entries to detect immediate emotional states and offer wellness recommendations.

#### 1.2 Scope
This system is an offline desktop-based software solution engineered for individuals, educational institutions, and corporate wellness modules. It uses core Natural Language Processing (NLP) to parse user sentiments without utilizing continuous cloud infrastructure, thereby securing complete data isolation.

---

### 2. General Description
#### 2.1 Product Perspective
The application operates as a standalone desktop utility executing completely within the local run-time domain of the user's operating system. 

#### 2.2 Product Functions
- **Text Ingestion:** Accepts real-time alphanumeric user entries.
- **Linguistic Analysis:** Tokenizes and extracts mood polarity metrics.
- **Dynamic Interface Adaptation:** Modifies UI theme colors dynamically based on psychological scores.
- **Rule-Based Recommendation Engine:** Delivers local behavioral tips (e.g., mindfulness reminders).

#### 2.3 User Classes and Characteristics
The primary end-users are students, working professionals, or individuals seeking regular personal emotional checks. No prior technical training is required to operate the minimalistic user interface.

#### 2.4 Design and Implementation Constraints
- **Language Constraints:** Built strictly using Python 3.x.
- **Data Privacy Constraints:** No external cloud API dependencies or network telemetry allowed for sentiment operations.
- **Hardware Limitations:** Must run efficiently on standard consumer hardware specifications (e.g., baseline execution tested on Intel Core Ultra architectures).

---

### 3. System Requirements & Tech Stack
The application depends on specific foundational substrates to execute properly:

- **GUI Framework:** `CustomTkinter` (Hardware-accelerated modern interface)
- **NLP Substrate:** `TextBlob` & `NLTK` (Lexicon-based syntactic analysis)
- **Environment Tooling:** Standard Python Virtual Environment (`venv`)

---

### 4. Functional Requirements
#### 4.1 UI Component Architecture
- **FR-1:** The system MUST initialize a clean dark-mode desktop window frame upon execution.
- **FR-2:** The application MUST provide a dedicated text entry layout capable of handling paragraph-length user inputs.

#### 4.2 NLP Processing Pipeline
- **FR-3:** The system MUST extract linguistic markers and return a numeric value $P$ bound between $-1.0 \le P \le 1.0$.
- **FR-4:** Analysis calculations MUST execute locally with a sub-second response latency.

#### 4.3 Behavioral Mapping Matrix
- **FR-5:** If $P < -0.2$, the system MUST update the dashboard background to soft red (`#ff7675`) and display high-stress warning actions.
- **FR-6:** If $-0.2 \le P \le 0.2$, the system MUST map the UI to soft yellow (`#fdcb6e`) and recommend standard biological homeostasis.
- **FR-7:** If $P > 0.2$, the system MUST trigger soft green (`#55efc4`) to represent optimal cognitive performance.

---

### 5. Non-Functional Requirements
#### 5.1 Security & Privacy
- Absolute data isolation is maintained. All user logs are strictly confined to the volatile memory space of the local application process.

#### 5.2 Performance & Reliability
- The application initialization sequence must complete within under 2 seconds.
- Memory consumption during active semantic string computations must remain under 150MB.

#### 5.3 Usability
- Minimalistic navigation control flow that requires exactly one user action click (`Analyze My Mood`) to render comprehensive analysis outputs.

---

### 6. Strategic Future Enhancements (Roadmap)
- **Acoustic Subsystem:** Integrating `Librosa` for real-time human voice frequency tracking.
- **Data Visualizer:** Incorporating localized `Matplotlib` modules for rendering descriptive graphical mood analytics history over time.
