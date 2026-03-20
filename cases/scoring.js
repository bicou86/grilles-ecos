
        // Déclaration des variables globales
        window.audioContext = null;

        // Chargement dynamique de srs.js
        (function() {
            var s = document.createElement('script');
            s.src = (location.pathname.indexOf('/cases/') >= 0 ? '../' : 'cases/') + 'srs.js';
            document.head.appendChild(s);
        })();
        
        function updateScore(section, element) {
            const value = element.value;
            const name = element.name;
            let pointValue;

            if (section === "communication") {
                const map = { A: 4, B: 3, C: 2, D: 1, E: 0 };
                pointValue = map[value] || 0;
                // Mettre à jour la classe de couleur pour communication
                const criteriaRow = document.getElementById("criteria-" + name);
                if (criteriaRow) {
                    criteriaRow.classList.remove("score-a", "score-b", "score-c", "score-d", "score-e", "lacune-rouge", "lacune-orange", "lacune-verte");
                    criteriaRow.classList.add("score-" + value.toLowerCase());
                    // Ajouter les classes lacune pour communication
                    if (value === "E" || value === "D") {
                        criteriaRow.classList.add("lacune-rouge");
                    } else if (value === "C") {
                        criteriaRow.classList.add("lacune-orange");
                    } else if (value === "A" || value === "B") {
                        criteriaRow.classList.add("lacune-verte");
                    }
                }
            } else {
                pointValue = Number(value) || 0;
                // Mettre à jour la classe de couleur pour autres critères
                const criteriaRow = document.getElementById("criteria-" + name);
                if (criteriaRow) {
                    criteriaRow.classList.remove("score-0", "score-1", "score-2", "lacune-rouge", "lacune-orange", "lacune-verte");
                    criteriaRow.classList.add("score-" + value);
                    // Ajouter les classes lacune pour critères normaux
                    if (pointValue === 0) {
                        criteriaRow.classList.add("lacune-rouge");
                    } else if (pointValue === 1) {
                        criteriaRow.classList.add("lacune-orange");
                    } else if (pointValue >= 2) {
                        criteriaRow.classList.add("lacune-verte");
                    }
                }
            }

            const pointsElement = document.getElementById("points-" + name);
            if (pointsElement) {
                pointsElement.textContent = pointValue;
            }

            calculateScores();
        }

        function updateDetailScore(criterionId, prefix) {
            let totalScore = 0;
            const detailCheckboxes = document.querySelectorAll('input[id^="' + criterionId + '-detail-"]');
            const maxDetailsScore = detailCheckboxes.length;
            
            detailCheckboxes.forEach(checkbox => {
                if (checkbox.checked) {
                    totalScore += Number(checkbox.value) || 0;
                }
            });
            
            const pointsElement = document.getElementById("points-" + criterionId);
            if (pointsElement) {
                pointsElement.textContent = totalScore;
            }
            
            // Mettre à jour la classe de couleur en fonction du score et du max
            const criteriaRow = document.getElementById("criteria-" + criterionId);
            if (criteriaRow) {
                criteriaRow.classList.remove("score-0", "score-1", "score-2", "score-3", "score-4", "score-5", "score-max", "lacune-rouge", "lacune-orange", "lacune-verte");
                
                // Déterminer la classe appropriée avec les seuils 1/3 et 2/3
                const oneThird = maxDetailsScore / 3;
                const twoThirds = (maxDetailsScore * 2) / 3;
                
                if (totalScore < oneThird) {
                    criteriaRow.classList.add("score-0");
                    criteriaRow.classList.add("lacune-rouge");
                } else if (totalScore > twoThirds) {
                    criteriaRow.classList.add("score-max");
                    criteriaRow.classList.add("lacune-verte");
                } else {
                    // Score entre 1/3 et 2/3
                    criteriaRow.classList.add("score-1");
                    criteriaRow.classList.add("lacune-orange");
                }
            }
            
            calculateScores();
        }

        function calculateScores() {
            const isNewFormat = false;
            const missingItems = [];
            let scores = {};
            let maxScores = {};
            let coef = {};
            let sectionInfo = [];

            // Per-case config loaded from inline script
            scores = {anamnese: 0, examen: 0, management: 0, communication: 0};
            maxScores = window.caseConfig.maxScores;
            coef = window.caseConfig.coef;
            sectionInfo = window.caseConfig.sectionInfo;

            // Calcul des scores pour chaque section
            sectionInfo.forEach(section => {
                let sectionScore = 0;
                
                if (section.isComm) {
                    // Section communication spéciale
                    for (let i = 1; i <= section.count; i++) {
                        const radio = document.querySelector("input[name=\"" + section.prefix + i + "\"]:checked");
                        if (radio) {
                            const val = radio.value;
                            const map = { A: 4, B: 3, C: 2, D: 1, E: 0 };
                            sectionScore += map[val] || 0;
                        } else {
                            const criteria = document.querySelector("input[name=\"" + section.prefix + i + "\"][data-criteria]");
                            if (criteria) missingItems.push(section.label + " : " + criteria.dataset.criteria);
                        }
                    }
                } else {
                    // Sections normales
                    for (let i = 1; i <= section.count; i++) {
                        const criterionId = section.prefix + i;
                        // Vérifier si ce critère a des détails avec checkboxes
                        const detailCheckboxes = document.querySelectorAll('input[id^="' + criterionId + '-detail-"]');
                        
                        if (detailCheckboxes.length > 0) {
                            // Ce critère a des détails, on calcule le score basé sur les détails
                            let detailScore = 0;
                            let hasCheckedDetail = false;
                            detailCheckboxes.forEach(checkbox => {
                                if (checkbox.checked) {
                                    detailScore += Number(checkbox.value) || 0;
                                    hasCheckedDetail = true;
                                }
                            });
                            sectionScore += detailScore;
                            
                            if (!hasCheckedDetail) {
                                const criteria = document.querySelector("input[name=\"" + criterionId + "\"][data-criteria]");
                                if (criteria) {
                                    missingItems.push(section.label + " : " + criteria.dataset.criteria);
                                } else {
                                    // Rechercher le texte du critère directement
                                    const criteriaText = document.querySelector("#criteria-" + criterionId + " .criteria-text");
                                    if (criteriaText) {
                                        missingItems.push(section.label + " : " + criteriaText.textContent.split(". ")[1].split(" [")[0]);
                                    }
                                }
                            }
                        } else {
                            // Critère normal sans détails
                            const radio = document.querySelector("input[name=\"" + criterionId + "\"]:checked");
                            if (radio) {
                                sectionScore += Number(radio.value) || 0;
                            } else {
                                const criteria = document.querySelector("input[name=\"" + criterionId + "\"][data-criteria]");
                                if (criteria) missingItems.push(section.label + " : " + criteria.dataset.criteria);
                            }
                        }
                    }
                }
                
                scores[section.key] = sectionScore;
                const scoreId = section.scoreId || section.key + "Score";
                const scoreElement = document.getElementById(scoreId);
                if (scoreElement) scoreElement.textContent = sectionScore;
            });

            // Calcul des pourcentages par section
            let percentages = {};
            let globalPercentage = 0;
            let isStarted = false;
            
            sectionInfo.forEach(section => {
                const score = scores[section.key];
                const max = maxScores[section.key];
                const percentage = max > 0 ? (score / max) * 100 : 0;
                percentages[section.key] = percentage;
                globalPercentage += percentage * coef[section.key];
                if (score > 0) isStarted = true;
            });

            const totalScoreText = isStarted ? Math.round(globalPercentage) : 0;
            document.getElementById("totalScore").textContent = totalScoreText + "%";

            // Mise à jour des pourcentages affichés
            sectionInfo.forEach(section => {
                const percentageElement = document.getElementById(section.key + "-percentage");
                if (percentageElement) {
                    percentageElement.textContent = Math.round(percentages[section.key]);
                }
            });

            const gradeElement = document.getElementById("globalGrade");
            const totalScoreElement = document.getElementById("totalScore");
            const scoreBody = totalScoreElement ? totalScoreElement.closest(".total-body") : null;
            const gradeBody = gradeElement ? gradeElement.closest(".total-body") : null;
            const sections = sectionInfo.map(s => s.key);

            const allClasses = ["note-a", "note-b", "note-c", "note-d", "note-e", "note-neutral"];

            function getClass(p) {
                if (p === 0) return "note-neutral";
                if (p >= 90) return "note-a";
                if (p >= 80) return "note-b";
                if (p >= 70) return "note-c";
                if (p >= 60) return "note-d";
                return "note-e";
            }

            const gradeClass = getClass(globalPercentage);
            const gradeLabel = isStarted ? gradeClass.split("-")[1].toUpperCase() : "A-E";
            if (gradeElement) gradeElement.textContent = gradeLabel;

            const pourcentBody = document.querySelector(".total-pourcent-body");

            [gradeElement, scoreBody, gradeBody, pourcentBody].forEach(el => {
                if (el) {
                    el.classList.remove(...allClasses);
                    el.classList.add(gradeClass);
                }
            });

            sections.forEach(id => {
                const percentageElement = document.getElementById(id + "-percentage");
                if (percentageElement) {
                    const value = parseInt(percentageElement.textContent);
                    const section = percentageElement.closest(".total-pourcent-section");
                    const sectionClass = getClass(value);
                    if (section) {
                        section.classList.remove(...allClasses);
                        section.classList.add(sectionClass);
                    }
                }
            });

            // Appliquer les couleurs aux sections principales
            sectionInfo.forEach(section => {
                const percentage = percentages[section.key];
                const allSections = document.querySelectorAll(".section");
                allSections.forEach(sectionEl => {
                    const headerText = sectionEl.querySelector(".section-header")?.textContent || "";
                    if (headerText.includes(section.label)) {
                        const sectionClass = getClass(percentage);
                        sectionEl.classList.remove(...allClasses);
                        sectionEl.classList.add(sectionClass);
                    }
                });
            });

            var missingEl = document.getElementById("missingItems");
            var missingListEl = document.getElementById("missingList");
            if (missingItems.length > 0) {
                if (missingEl) missingEl.style.display = "block";
                if (missingListEl) missingListEl.innerHTML = missingItems.map(item =>
                    "<div class=\"missing-item\">• " + item + "</div>"
                ).join("");
            } else {
                if (missingEl) missingEl.style.display = "none";
            }

            // Save score to central registry for dashboard
            saveToRegistry(globalPercentage, isStarted);
        }
        // MINUTEUR ECOS 13 MINUTES
        window.timerInterval = null;
        window.currentSeconds = 13 * 60;
        window.isRunning = false;
        window.hasStarted = false;
        window.hasFinished = false;
        window.hasStoppedManually = false;

        window.currentMode = 'revision';

        function colorPatientResponses() {
            // Version simplifiée inspirée du générateur v1
            const elements = document.querySelectorAll('.criteria-text, .sub-criteria, .redflags-text, .dd-item, .therapy-section, .detail-text, .cloture-content');
            elements.forEach(element => {
                const text = element.innerHTML;
                // Colorer uniquement les réponses patient en bleu (pas les examens complémentaires)
                let coloredText = text.replace(/\[([^\]]+)\]/g, '<span style="color: rgb(44, 90, 160); font-weight: 500;">[$1]</span>');
                element.innerHTML = coloredText;
            });
        }

        // === CIRCUIT MODE DETECTION ===
        window.circuitMode = false;
        (function() {
            try {
                var raw = localStorage.getItem('ecos_circuit');
                if (raw) {
                    var circuit = JSON.parse(raw);
                    if (circuit && circuit.phase === 'station') {
                        window.circuitMode = true;
                    }
                }
            } catch(e) {}
        })();

        document.addEventListener('DOMContentLoaded', function() {
            if (window.circuitMode) {
                // Circuit mode: auto-start in exam mode
                switchMode('exam');
                calculateScores();
                colorPatientResponses();
                // Hide mode selector and nav bar in circuit mode
                var modeSelector = document.querySelector('.mode-selector');
                if (modeSelector) modeSelector.style.display = 'none';
                // Show circuit nav instead of normal nav
                createCircuitNav();
                // Auto-start timer after short delay
                setTimeout(function() { startTimer(); }, 500);
            } else {
                switchMode('revision');
                calculateScores();
                colorPatientResponses();
                createNavBar();
            }
            // Appeler une deuxième fois après un court délai pour s'assurer que tout est chargé
            setTimeout(function() {
                colorPatientResponses();
            }, 100);
            // Appel supplémentaire après un délai plus long pour garantir que tout est chargé
            setTimeout(function() {
                colorPatientResponses();
            }, 500);
            // Auto-resize tous les textareas au chargement
            const allTextareas = document.querySelectorAll('.comment-textarea');
            allTextareas.forEach(textarea => {
                if (textarea.value) {
                    autoResizeTextarea(textarea);
                }
            });
        });
        
        // S'assurer que la hauteur est bien définie avant l'impression
        window.addEventListener('beforeprint', function() {
            const allTextareas = document.querySelectorAll('.comment-textarea');
            allTextareas.forEach(textarea => {
                if (textarea.value && textarea.value.trim()) {
                    // S'assurer que le textarea a une hauteur définie
                    if (!textarea.style.height || textarea.style.height === 'auto') {
                        autoResizeTextarea(textarea);
                    }
                }
            });
        });


        function initAudio() {
            if (!window.audioContext) {
                window.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playBeep() {
            initAudio();
            const oscillator = window.audioContext.createOscillator();
            const gainNode = window.audioContext.createGain();
            oscillator.connect(gainNode);
            gainNode.connect(window.audioContext.destination);
            oscillator.frequency.value = 800;
            oscillator.type = 'sine';
            gainNode.gain.setValueAtTime(0.3, window.audioContext.currentTime);
            gainNode.gain.exponentialRampToValueAtTime(0.01, window.audioContext.currentTime + 0.5);
            oscillator.start(window.audioContext.currentTime);
            oscillator.stop(window.audioContext.currentTime + 0.5);
        }

        function speak(text) {
            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'fr-FR';
                utterance.rate = 0.9;
                utterance.volume = 0.8;
                speechSynthesis.speak(utterance);
            }
        }

        function playSound(message) {
            playBeep();
            setTimeout(() => speak(message), 500);
        }

        function formatTime(seconds) {
            const minutes = Math.floor(seconds / 60);
            const secs = seconds % 60;
            return minutes + ":" + secs.toString().padStart(2, "0");
        }

        function toggleCheckboxes(disabled) {
            const radios = document.querySelectorAll('input[type="radio"]');
            radios.forEach(radio => {
                radio.disabled = disabled;
            });
            const detailCheckboxes = document.querySelectorAll('.detail-checkbox input[type="checkbox"]');
            detailCheckboxes.forEach(checkbox => {
                checkbox.disabled = disabled;
            });
        }

        function colorCriteriaByScore() {
            if (!window.hasFinished && !window.hasStoppedManually) return;

            const normalCriteriaRows = document.querySelectorAll('.criteria-row');
            normalCriteriaRows.forEach(row => {
                const id = row.id;
                if (!id) return;
                const criteriaName = id.replace('criteria-', '');
                const checkedRadio = document.querySelector('input[name="' + criteriaName + '"]:checked');
                row.classList.remove('criteria-zero-points', 'criteria-one-point', 'criteria-full-points', 'criteria-not-answered', 'lacune-rouge', 'lacune-orange', 'lacune-verte');
                if (checkedRadio) {
                    const score = Number(checkedRadio.value) || 0;
                    if (score === 0) {
                        row.classList.add('criteria-zero-points');
                        row.classList.add('lacune-rouge');
                    } else if (score === 1) {
                        row.classList.add('criteria-one-point');
                        row.classList.add('lacune-orange');
                    } else if (score >= 2) {
                        row.classList.add('criteria-full-points');
                        row.classList.add('lacune-verte');
                    }
                } else {
                    row.classList.add('criteria-not-answered');
                    row.classList.add('lacune-rouge');
                }
            });

            const communicationRows = document.querySelectorAll('.communication-section');
            communicationRows.forEach(row => {
                const id = row.id;
                if (!id) return;
                const criteriaName = id.replace('criteria-', '');
                const checkedRadio = document.querySelector('input[name="' + criteriaName + '"]:checked');
                row.classList.remove('communication-note-a', 'communication-note-b', 'communication-note-c', 'communication-note-d', 'communication-note-e', 'communication-not-answered', 'lacune-rouge', 'lacune-orange', 'lacune-verte');
                if (checkedRadio) {
                    const grade = checkedRadio.value.toLowerCase();
                    row.classList.add("communication-note-" + grade);
                    if (grade === 'e' || grade === 'd') {
                        row.classList.add('lacune-rouge');
                    } else if (grade === 'c') {
                        row.classList.add('lacune-orange');
                    } else if (grade === 'a' || grade === 'b') {
                        row.classList.add('lacune-verte');
                    }
                } else {
                    row.classList.add('communication-not-answered');
                    row.classList.add('lacune-rouge');
                }
            });
        }

        function startTimer() {
            if (window.isRunning || window.currentMode !== 'exam') return;
            window.isRunning = true;
            window.hasStarted = true;
            window.hasStoppedManually = false;
            document.body.classList.add('timer-running');
            toggleCheckboxes(false);
            playSound("Début de la station");
            document.getElementById('startBtn').style.display = 'none';
            document.getElementById('stopBtn').style.display = 'inline-block';
            document.getElementById('resetBtn').disabled = true;
            document.getElementById('timerStatus').textContent = 'En cours';
            document.getElementById('timerStatus').className = 'timer-status status-running';
            
            window.timerInterval = setInterval(() => {
                window.currentSeconds--;
                document.getElementById('timerDisplay').textContent = formatTime(window.currentSeconds);
                const container = document.getElementById('timerContainer');
                if (window.currentSeconds === 2 * 60) {
                    if (window.currentMode === 'exam') {
                        playSound("Il vous reste 2 minutes");
                    }
                    container.classList.add('timer-warning');
                    document.getElementById('timerStatus').textContent = '2 min restantes';
                    document.getElementById('timerStatus').className = 'timer-status status-warning';
                }
                if (window.currentSeconds <= 30) {
                    container.classList.add('timer-critical');
                }
                if (window.currentSeconds <= 0) {
                    endTimer();
                }
            }, 1000);
        }

        function stopTimer() {
            if (!window.isRunning) return;
            clearInterval(window.timerInterval);
            window.isRunning = false;
            window.hasStoppedManually = true;
            document.body.classList.remove('timer-running');
            // Ne pas désactiver les checkboxes pour permettre de continuer à cocher après arrêt
            // toggleCheckboxes(true);
            document.getElementById('startBtn').style.display = 'inline-block';
            document.getElementById('stopBtn').style.display = 'none';
            document.getElementById('resetBtn').disabled = false;
            document.getElementById('timerStatus').textContent = 'Arrêté';
            document.getElementById('timerStatus').className = 'timer-status';
            colorCriteriaByScore();
        }

        function endTimer() {
            clearInterval(window.timerInterval);
            window.isRunning = false;
            window.hasFinished = true;
            window.currentSeconds = 0;
            document.body.classList.remove('timer-running');
            if (window.currentMode === 'exam') {
                playSound("Fin de la station. Veuillez sortir");
                // In circuit mode: save score and return to exam.html
                if (window.circuitMode) {
                    // Force score calculation and save before navigating
                    calculateScores();
                    // Mark circuit as returning
                    try {
                        var raw = localStorage.getItem('ecos_circuit');
                        if (raw) {
                            var circuit = JSON.parse(raw);
                            circuit.phase = 'returning';
                            localStorage.setItem('ecos_circuit', JSON.stringify(circuit));
                        }
                    } catch(e) {}
                    // Navigate back to exam page after a short delay for score save
                    setTimeout(function() {
                        window.location.href = '../../exam.html';
                    }, 2000);
                    return;
                }
                // Repasser automatiquement en mode révision après la fin du timer
                switchMode('revision');
            }
            document.getElementById('timerDisplay').textContent = '0:00';
            document.getElementById('startBtn').style.display = 'inline-block';
            document.getElementById('stopBtn').style.display = 'none';
            document.getElementById('resetBtn').disabled = false;
            document.getElementById('timerStatus').textContent = 'Terminé';
            document.getElementById('timerStatus').className = 'timer-status status-finished';
            document.getElementById('timerStatus').style.display = 'block';
            document.getElementById('timerContainer').className = 'timer-container';
            // Ne pas désactiver les checkboxes après la fin pour permettre de continuer
            // toggleCheckboxes(true);
            colorCriteriaByScore();
        }

        function resetTimer() {
            clearInterval(window.timerInterval);
            window.timerInterval = null;
            window.currentSeconds = 13 * 60;
            window.isRunning = false;
            window.hasStarted = false;
            window.hasFinished = false;
            window.hasStoppedManually = false;
            document.getElementById('timerDisplay').textContent = '13:00';
            document.getElementById('startBtn').style.display = 'inline-block';
            document.getElementById('stopBtn').style.display = 'none';
            // Supprimer la coloration des critères
            const criteriaAndCommRows = document.querySelectorAll('.criteria-row, .communication-section');
            criteriaAndCommRows.forEach(row => {
                row.classList.remove('score-0', 'score-1', 'score-2', 'score-a', 'score-b', 'score-c', 'score-d', 'score-e');
            });
            // Supprimer la coloration des sections
            const allSections = document.querySelectorAll('.section');
            allSections.forEach(section => {
                section.classList.remove('note-a', 'note-b', 'note-c', 'note-d', 'note-e');
                section.classList.add('note-neutral');
            });
            document.getElementById('timerStatus').style.display = 'none';
            document.getElementById('timerContainer').className = 'timer-container';
            // En mode révision, ne pas désactiver les checkboxes
            if (window.currentMode === 'exam') {
                toggleCheckboxes(true);
            }
            const allRadios = document.querySelectorAll('input[type="radio"]');
            allRadios.forEach(radio => {
                radio.checked = false;
            });
            // Réinitialiser les detail-checkboxes
            const allDetailCheckboxes = document.querySelectorAll('.detail-checkbox input[type="checkbox"]');
            allDetailCheckboxes.forEach(checkbox => {
                checkbox.checked = false;
            });
            const allPointsDisplays = document.querySelectorAll('.points-display');
            allPointsDisplays.forEach(display => {
                display.textContent = '0';
            });
            const allCriteriaRows = document.querySelectorAll('.criteria-row');
            allCriteriaRows.forEach(row => {
                row.classList.remove('criteria-zero-points', 'criteria-one-point', 'criteria-full-points', 'criteria-not-answered', 'lacune-rouge', 'lacune-orange', 'lacune-verte');
            });
            const allCommunicationRows = document.querySelectorAll('.communication-section');
            allCommunicationRows.forEach(row => {
                row.classList.remove('communication-note-a', 'communication-note-b', 'communication-note-c', 'communication-note-d', 'communication-note-e', 'communication-not-answered', 'lacune-rouge', 'lacune-orange', 'lacune-verte');
            });
            calculateScores();
            // Supprimer tous les commentaires et cacher les textareas
            const allTextareas = document.querySelectorAll('.comment-textarea');
            allTextareas.forEach(textarea => {
                textarea.value = '';
                textarea.style.height = textarea.classList.contains('comment-textarea') && textarea.closest('.section-comment-section.global') ? '30px' : (textarea.closest('.section-comment-section') ? '28px' : '26px');
            });
            // Cacher toutes les sections de commentaires ouvertes
            const allCommentSections = document.querySelectorAll('.criterion-comment-section.show, .section-comment-section.show');
            allCommentSections.forEach(section => {
                section.classList.remove('show');
            });
            // Mettre à jour les boutons de commentaires
            const allCommentButtons = document.querySelectorAll('.comment-button, .section-comment-button');
            allCommentButtons.forEach(button => {
                button.classList.remove('has-content');
            });
        }
        
        function switchMode(mode) {
            window.currentMode = mode;
            const body = document.body;
            body.className = mode + '-mode';
            const buttons = document.querySelectorAll('.mode-button');
            buttons.forEach(btn => btn.classList.remove('active'));
            buttons.forEach(btn => {
                if (btn.textContent.includes(mode === "revision" ? "Révision" : "Examen")) {
                    btn.classList.add("active");
                }
            });
            if (mode === 'revision') {
                toggleCheckboxes(false);
                showLacunesButton();
            } else {
                if (!window.hasStarted) {
                    toggleCheckboxes(true);
                }
                hideLacunesButton();
            }
        }
        
        function showLacunesButton() {
            const btn = document.querySelector('.lacune-button');
            if (btn) btn.style.display = 'block';
        }
        
        function hideLacunesButton() {
            const btn = document.querySelector('.lacune-button');
            if (btn) btn.style.display = 'none';
        }
        
        function identifyLacunes() {
            // Critères standards (anamnèse, examen, management)
            const criteria = document.querySelectorAll(".criteria-row");
            criteria.forEach(criterion => {
                const id = criterion.id.replace("criteria-", "");
                const pointsElement = document.getElementById("points-" + id);
                const points = pointsElement ? parseInt(pointsElement.textContent) : 0;
                
                criterion.classList.remove("lacune-rouge", "lacune-orange", "lacune-verte");
                
                if (points === 0) {
                    criterion.classList.add("lacune-rouge");
                } else if (points === 1) {
                    criterion.classList.add("lacune-orange");
                } else if (points >= 2) {
                    criterion.classList.add("lacune-verte");
                }
            });
            
            // Critères communication (échelle A-E)
            const commCriteria = document.querySelectorAll(".communication-section");
            commCriteria.forEach(criterion => {
                const id = criterion.id.replace("criteria-", "");
                const radio = document.querySelector("input[name=\"" + id + "\"]:checked");
                
                criterion.classList.remove("lacune-rouge", "lacune-orange", "lacune-verte");
                
                if (!radio) {
                    criterion.classList.add("lacune-rouge");
                } else {
                    const grade = radio.value;
                    if (grade === "E" || grade === "D") {
                        criterion.classList.add("lacune-rouge");
                    } else if (grade === "C") {
                        criterion.classList.add("lacune-orange");
                    } else if (grade === "A" || grade === "B") {
                        criterion.classList.add("lacune-verte");
                    }
                }
            });
        }
        function toggleComment(id) {
            const section = document.getElementById("comment-section-" + id);
            const textarea = document.getElementById("comment-" + id);
            if (section) {
                section.classList.toggle("show");
                // Focus automatiquement sur le textarea quand on ouvre la section
                if (section.classList.contains("show") && textarea) {
                    textarea.focus();
                }
            }
        }

        function updateCommentButton(id) {
            const textarea = document.getElementById("comment-" + id);
            const criterionRow = document.getElementById("criteria-" + id);
            const commentSection = document.getElementById("comment-section-" + id);
            if (textarea && criterionRow) {
                const button = criterionRow.querySelector(".comment-button");
                if (button) {
                    if (textarea.value.trim()) {
                        button.classList.add("has-content");
                        if (commentSection) commentSection.classList.add("has-content");
                    } else {
                        button.classList.remove("has-content");
                        if (commentSection) commentSection.classList.remove("has-content");
                    }
                }
            }
        }

        function toggleSectionComment(section) {
            const commentSection = document.getElementById("section-comment-" + section);
            const textarea = document.getElementById("comment-section-" + section);
            if (commentSection) {
                commentSection.classList.toggle("show");
                // Focus automatiquement sur le textarea quand on ouvre la section
                if (commentSection.classList.contains("show") && textarea) {
                    textarea.focus();
                }
            }
        }

        function updateSectionComment(section) {
            const textarea = document.getElementById("comment-section-" + section);
            const commentSection = document.getElementById("section-comment-" + section);
            const buttons = document.querySelectorAll(".section-comment-button");
            buttons.forEach(button => {
                if (button.getAttribute("onclick") && button.getAttribute("onclick").includes(section)) {
                    if (textarea && textarea.value.trim()) {
                        button.classList.add("has-content");
                        if (commentSection) commentSection.classList.add("has-content");
                    } else {
                        button.classList.remove("has-content");
                        if (commentSection) commentSection.classList.remove("has-content");
                    }
                }
            });
        }

        function updateGeneralComment() {
            const textarea = document.getElementById("comment-general");
            if (textarea) {
                const section = textarea.closest(".section-comment-section");
                if (section) {
                    if (textarea.value.trim()) {
                        section.classList.add("has-content");
                    } else {
                        section.classList.remove("has-content");
                    }
                }
            }
        }

        function autoResizeTextarea(textarea) {
            // Reset height to auto to get correct scrollHeight
            textarea.style.height = "auto";
            // Set new height based on content
            const newHeight = textarea.scrollHeight + 2;
            textarea.style.height = newHeight + "px";
        }

    


        // === CENTRAL SCORE REGISTRY ===
        function saveToRegistry(globalPercentage, isStarted) {
            if (!isStarted) return;
            var pageFile = location.pathname.split("/").pop().replace(/\.html$/, "");
            var gradeEl = document.getElementById("globalGrade");
            var pct = Math.round(globalPercentage) || 0;
            var grade = gradeEl ? gradeEl.textContent.trim() : "";
            if (pct === 0 && grade === "A-E") return;

            var registry = {};
            try { registry = JSON.parse(localStorage.getItem("ecos_registry") || "{}"); } catch(e) {}
            var existing = registry[pageFile] || {};
            registry[pageFile] = {
                pct: pct,
                grade: grade,
                best: Math.max(existing.best || 0, pct),
                date: new Date().toISOString()
            };
            try { localStorage.setItem("ecos_registry", JSON.stringify(registry)); } catch(e) {}

            // Update spaced repetition data
            if (typeof SRS !== 'undefined' && SRS.update) {
                SRS.update(pageFile, grade);
            }
        }

        // === NAVIGATION BAR ===
        function createNavBar() {
            var caseIndex = [];
            try { caseIndex = JSON.parse(localStorage.getItem("ecos_case_index") || "[]"); } catch(e) {}

            var currentFile = location.pathname.split("/").pop();
            var currentIdx = -1;
            for (var i = 0; i < caseIndex.length; i++) {
                if (caseIndex[i].url.endsWith(currentFile)) {
                    currentIdx = i;
                    break;
                }
            }

            var nav = document.createElement("div");
            nav.className = "case-nav-bar";

            // Back button
            var back = document.createElement("a");
            back.href = "../../index.html";
            back.className = "nav-back";
            back.textContent = "\u2190 Retour";
            nav.appendChild(back);

            if (currentIdx >= 0) {
                // Prev arrow
                var prev = document.createElement("a");
                if (currentIdx > 0) {
                    prev.href = "../../" + caseIndex[currentIdx - 1].url;
                    prev.title = caseIndex[currentIdx - 1].title;
                } else {
                    prev.className = "disabled";
                }
                prev.classList.add("nav-arrow");
                prev.textContent = "\u2039";
                nav.appendChild(prev);

                // Position indicator
                var pos = document.createElement("span");
                pos.className = "nav-position";
                pos.textContent = (currentIdx + 1) + " / " + caseIndex.length;
                nav.appendChild(pos);

                // Next arrow
                var next = document.createElement("a");
                if (currentIdx < caseIndex.length - 1) {
                    next.href = "../../" + caseIndex[currentIdx + 1].url;
                    next.title = caseIndex[currentIdx + 1].title;
                } else {
                    next.className = "disabled";
                }
                next.classList.add("nav-arrow");
                next.textContent = "\u203A";
                nav.appendChild(next);
            }

            document.body.insertBefore(nav, document.body.firstChild);
        }

        // === CIRCUIT NAVIGATION BAR ===
        function createCircuitNav() {
            var circuit = null;
            try { circuit = JSON.parse(localStorage.getItem('ecos_circuit')); } catch(e) {}
            if (!circuit) { createNavBar(); return; }

            var nav = document.createElement("div");
            nav.className = "case-nav-bar";

            // Station label
            var label = document.createElement("span");
            label.className = "nav-position";
            label.style.fontWeight = "700";
            label.textContent = "Station " + (circuit.current + 1) + " / " + circuit.stations.length;
            nav.appendChild(label);

            // Quit button
            var quit = document.createElement("a");
            quit.href = "#";
            quit.className = "nav-back";
            quit.textContent = "Quitter l\u2019examen";
            quit.style.marginLeft = "auto";
            quit.addEventListener("click", function(e) {
                e.preventDefault();
                if (confirm("Quitter l\u2019examen en cours ?")) {
                    // Save score and return
                    calculateScores();
                    try {
                        var raw = localStorage.getItem('ecos_circuit');
                        if (raw) {
                            var c = JSON.parse(raw);
                            c.phase = 'returning';
                            localStorage.setItem('ecos_circuit', JSON.stringify(c));
                        }
                    } catch(ex) {}
                    window.location.href = '../../exam.html';
                }
            });
            nav.appendChild(quit);

            // Finish station button (manual advance)
            var finish = document.createElement("a");
            finish.href = "#";
            finish.className = "nav-back";
            finish.style.background = "#16a34a";
            finish.style.color = "white";
            finish.style.borderRadius = "6px";
            finish.style.padding = "0.3rem 0.7rem";
            finish.textContent = "Terminer la station \u2192";
            finish.addEventListener("click", function(e) {
                e.preventDefault();
                if (window.isRunning) stopTimer();
                calculateScores();
                try {
                    var raw = localStorage.getItem('ecos_circuit');
                    if (raw) {
                        var c = JSON.parse(raw);
                        c.phase = 'returning';
                        localStorage.setItem('ecos_circuit', JSON.stringify(c));
                    }
                } catch(ex) {}
                window.location.href = '../../exam.html';
            });
            nav.appendChild(finish);

            document.body.insertBefore(nav, document.body.firstChild);
        }

        // Appel final pour s'assurer que tout est coloré
        // Forcer la coloration finale
        if (window.colorPatientResponses) {
            window.colorPatientResponses();
        }
    