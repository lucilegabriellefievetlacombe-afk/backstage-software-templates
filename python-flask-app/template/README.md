# ${{values.name}}

- [${{values.name}}](#valuesname)
  - [${{values.uid}}](#valuesuid)
  - [Application documentation](#application-documentation)
  - [Zen Programmin (ZP)](#zen-programmin-zp)
    - [Cycle](#cycle)
    - [Values](#values)
    - [Tactics](#tactics)
  - [**TAZ** -  **T**eam **A**gile **Z**en](#taz----team-agile-zen)
    - [**POMO** - **P**roduct **O**wner \& **M**ilestones **O**rchestrator:](#pomo---product-owner--milestones-orchestrator)
    - [**QAAT** - **Q**uality **A**ssement \& **A**cceptance **T**ests:](#qaat---quality-assement--acceptance-tests)
    - [**TAM** - **Technical**  **A**rchitect \& **M**aintainer:](#tam---technical--architect--maintainer)
    - [**DEX** - **D**evelopers **EX**perts:](#dex---developers-experts)
    - [**GitOps** - **G**it**O**ps:](#gitops---gitops)
    - [**AgileMonk** - **A**gile **M**onk:](#agilemonk---agile-monk)
  - [Git Branchs](#git-branchs)

## ${{values.uid}}

- deployment environements : ${{values.environements}}
- owner: ${{values.owner}}

## Application documentation

[DOC](docs/index.md)

## Zen Programmin (ZP)

### Cycle

1. Fonctional requirements overview and main epics identification.
2. Cosy IDP with gitOps best practices.
3. Business Glossary.
4. General Functional Specifications:
   1. Roles & Business Entities.
   2. Use Cases.
   3. Story boards.
   4. CRC (Class, Responsibility, Collaborator) & Sequence diagrams.
5. Technical Requirements, Epics, Specifications, Best Practices docs.
6. Requirements Prioritization & Risk estimation
7. Sprints Iteration :
   1. User Stories (US) definition, CRC (Class, Responsibility, Collaborator) & raffinement.
   2. Tasks Prioritization & Risk estimation.
   3. Realistic Developer-EXperts (DEX) pocker planning.
   4. Tierce Daily Ceremonies Cosy Communication.
   5. Continuous Task Validation & Delivery in user story (US) environement demonstartion (DEMO).
   6. Continuous integration branch acceptance testing in qualification (QAL) environment.
   7. alpha-release validation phase:
      1. Refactoring, vendors updates & code cleanning of integration branch.
      2. alpha-release acceptance testing (AT) in AT pre-production (PPD) environment.
      3. alpha-release system testing (ST) in ST pre-production (PPD) environment .
      4. publication in producton (PROD) environment.
   8. Retro & Team work valorization

### Values

1. Respect of all teams.
2. Help each-others.
3. Don't be afraid.
4. Don't blame.

### Tactics

1. Auto organisation of developpers and experts for duo or trio programming.
2. Repetitive task automation.
3. One source of truth in one documentation.
4. Simple and clear, not fuzzy, not duplicated specification.
5. Test, try and refine.
6. Don't blame, help, keep things simple and be clear.
7. Give feed backs quickly.

## **TAZ** -  **T**eam **A**gile **Z**en

[**POMO**](#pomo---product-owner-milestones-orchestrator) | 
[**QAAT**](#qaat---quality-assement-acceptance-tests) | 
[**TAM**](#tam---technical--architect--maintainer) | 
[**DEX**](#dex---developers-experts) | 
[**GitOps**](#gitops---gitops) | 
[**AgileMonk**](#agilemonk---agile-monk)

### **POMO** - **P**roduct **O**wner & **M**ilestones **O**rchestrator:

Final Product Responsable - **Decide how the product must work for final users**.
Supervise functional requirements, specification redaction and features tasks redaction.
Schedule and orchestrate the project advancement.
Validate functional tasks understanding and implementation.

* **Functional Specifications Redaction** :
  * Responsable for introduction and global project description.
  * Responsible for business terms glossary:
    * definition.
    * disambiguation.
    * deduplication.
    * acronym if practical.
  * Responsable for general functional specifications.
    * Roles
    * Business entites
    * Use Cases, sequence diagrams.
    * Mockups
    * Story Boards
  * Take in account technical specification constraints and requirements.
* **Manage Fonctional Epics and Milestones** (taking in account technicals necessities).
  * Organise general specifications into Epics.
  * Priorize Epics.
  * Schedule Epics progression in Milestones.
* **Manage Requirements** :
  * Organise functionnal requirements :
    * Requirement UID - **RUID**
      * UID nomenclature is linked to epics or specification and milestones in a way that does not creates doublon and faciltate understanding : ex BACK-LOGIN-ADMIN-app_base, FRONT-LOGIN-USER-app_base, BACK-ADD-CATALOG-ARTICLE-app_poc, BACK-ADD-ARTICLE-IDENTIFICATION-app_poc, BACK-ADD-ARTICLE-STOCK-app_poc, FRONT-CUSTOMER-CART-app_poc, FRONT-ARTICLE-VIEW-app_poc, FRONT-ARTICLES-LIST-app_demo.
    * Related Epics.
    * Short description.
    * Related general or detailed specification version, chapter, section and **User Story**.
    * Fonctional Priority.
    * Risk.
    * Related MileStones & links to them.
    * Spec Avancement & links to them.
    * Code Avancement & links to them.
    * Test coverage Avancement & links to them.
    * Automated test coverage Avancement & Links to them.
  * Follow all requirements advancement.
* Responsable for **detailed functional specifications** in **User Stories**.
  * Main RUID, linked RUIDs
  * Context : HMI page or CLI command, user roles, global action, entities, status, steps or events.
  * what is the trigger action ?
  * what is the expected result ?
  * global description of how to test it is working ?
* **Fonctional Tasks Redaction** :
  * Validate the DoR and DoD with the Maintainer and the dev-team.
  * Create **func-spec/*RUID*-x** functional specification tasks.
    * Feature description :
      * Requirement uid selection should add :
        * Ref & Link to RUID. 
        * Related general specification version, chapter, section and **user story** link.
        * Tests list and links.
      * some fixtures and an example.
    * Ensure the developers got a good understanding of the new features.
    * Ensure there is no task duplicatas.
* **Feature Fonctional Unit Tests & Validation**.
* Create **fix/*RUID*-x** **fix** or **hotfix** subtasks.
  * describe the bug or refining for **func-spec/*RUID*-x**.
  * if needed add additional tests.
  * if it is blocking the production :
    * add label hotfix to the task.
    * ping and assign any hotfix to the maintainer.
* **Orchestration** :
  * Give the GO to the next **Milestone**.
  * Give the GO for the new **Sprint**.
  * Give the GO for **features POC or development tasks** (after DoR ok).
  * Give the GO for **features code review** (after feature functional unit testing).
  * Give the GO for **alpha release** with the QA (after QA has done acceptance tests).
  * Give the GO for **MEP** with the maintainer (after maintainer systems tests in PPD).
  * Ask MEP potential rollback.
  * Give the GO for **QA test** strategy, tactics and acceptance test plans.
  * Give the GO for **test automation** strategy, tactics and tasks.
  * Give the GO for **refactoring** strategy, tactics and tasks.

### **QAAT** - **Q**uality **A**ssement & **A**cceptance **T**ests:

QA Acceptance tests responsables - Validate applications are working and respects specifications.

* Participate to the **functional testing automation** strategy and tactics with the maintainer.
* Responsible for **acceptance tests** strategy, tactics and plan.
* **Manage Acceptance Tests Epics and Milestones.**
* **Blur hunting** :
  * Ask details and explanations about specifications.
  * Ask glossary term clarification, disambiguation and deduplication.
* Ask fixtures for testing.
* Validate acceptance testing plan with PO.
* Make Acceptance tests (with requirements uid) in QA integration env.
* **Validate** the integration develop branch (alpha release).
* Open bug issues with the PO.
* Give the **GO for alpha release** with the PO.
* Create test automation tasks.
* Share their automated tests with the dev-team (shifleft).
  
### **TAM** - **Technical**  **A**rchitect & **M**aintainer:

Technical Maintainer & Architect who lead the tech teams. Supervise good pratices enforcement and IDP improvements.
Decide for the global technical architectures and support technical teams for specifications and implementation.
Supervise deployments automation in Feature Demo, QA, PPD and MEP environements.
Manage code reviews, code update, merge request, merges and conflicts.

*The merge conflicts might be a source of chaotic behaviours, the dev-team must be protected from conflicts. The mini-task-teams work evaluation must not be impacted by code conflicts. If work evaluation was impacted, it would permit conflict makers to look faster and more efficients than impacted ones.*

* **Best technical pratices advocate**.
* **Lead the global technical specifications**.
  * Validate features technical specifications.
  * Anticipate and manage code conflicts or doublons.
* **Manage Technical Epics and Milestones.**
* **Organise technical requirements (according to functional needs)** :
  * Requirement UID - **RUID**
    * UID nomenclature is linked to epics or specification and milestones in a way that does not creates doublon and faciltate understanding : ex AUTH-ADMIN-system_base, MONITOR-DB-system_base, MONITOR-APP-system_base, AUTH-USER_app_base, LOG-APP-app_base, LOG-USER-ACTIONS_app_base, LOG-CATALOG-EVENTS_app_base LOG-ARTICLE-STOCK_app_base...
  * Theme.
  * Related Epics (all).
  * Short description.
  * Related general or detailed functional & technicals specifications version, chapter, section...
  * Linked Fonctional Priority.
  * Technical Priority.
  * Risk.
  * Related MileStones & links to them.
  * Spec Avancement & links to them.
  * Code Avancement & links to them.
  * Test coverage Avancement & links to them.
  * Automated test coverage Avancement & Links to them.
* Follow all requirements advancement.
* **Technical Helper** :
  * Help developers to use IDP.
  * Help developers to solve technical difficulties.
  * Help developers for technical specifications redaction.
  * Help QA to get adapted fixtures and cosy testing environements.
  * Help PO, participate to DoR and DoD with the dev-team.
* **IDP Responsable** :
  * Set & check technical constraints.
  * GitOps or GitOps main contact.
  * Keep Internal Development Plateform cosy.
* **Code review & Merge** :
  * Validate code reviews.
  * Merge features and fix in the develop integration branch (*).
    * The maintainer check updates and merges potentials conflicts :
      * If not any conflicts and regressions, it is merged.
      * If there is small conflicts the maintainer resolve them, pass tests and merge.
      * If another tasks made major conflicts :
        * conflict task is created
        * gitblame tel witch task is in conflict
        * **conflict/*RUID*-x_*RUID*-y** subtask and branch is created
        * gitblame tel who will participate to this task
  * Verifiy the develop branch is always globally functional and allow to start developments.
* **Relases Deployment & MEP**
  * Do or supervise creation and deployment of the alpha release branchs.
  * Do or supervise creation and deployment of the latest releases in PPD.
  * Do or Supervise system tests before MEP.
  * Do or Supervise the MEP with the PO GO.
* **Hotfix**
  * **hotfix/*RUID*-x** branch might be created from the main branch by the PO (from hotfix subtask creation).
  * The maintainer supervise or resolve the hotfix and hot related MEP.
  * The corresponding fix task branch have been created from develop branch.
* **TDD Lead**
  * Set the unit testing automation strategy and tactics with the dev-team.
  * Set the functional testing automation strategy and tactics with the QA.
  * Set the testing priority with the PO and the QA.
  * Keep requirements test automation list.
  * Creates automation testing tasks.
* **Refactoring Lead**
  * Creates refactoring strategy and tactics.
  * Validate refactoring strategy, tactics and priorities with the dev-team and PO.
  * Create refactor tasks.
* If CI/CD, performance optimizations or dependencies updates are needed some **ci/*RUID*-x** **perf/*RUID*-x** or **chlore/*RUID*-x** tasks and branchs might be created by the MA.
  
### **DEX** - **D**evelopers **EX**perts:

Developers and technical experts, responsable for their features technical specification and implementation.
Validate specification redaction respect DoR.
Participate to the DoR and DoD elabration. Source of proposals for IDP, tasks board improvements and technologies choices.
Auto-organise in duo or trio mini task teams.

* **Best development practices advocate.**
* Cultivate a particular domain of expertise (a language, orm, ia, bigdata, brocker...)
* Help other developers.
* Participate to tests automation and refactory strats and tactics.
* Ask for cosy IDP, make practical proposals to the mainatiner.
* Participate to backlog features reviews :
  * Ask for feature details.
  * Validate feature task with the DoR.
  * Ask for POC if time estimation is too complex.
  * Or Estimate tasks difficulty, risk level and time.
  * Split big tasks.
* Adopt a feature (or a refato) alone, or in a duo or trio mini team.
  * Auto-organise RASIC for duo/pair or trinome/trio task team.
  * Task and subtasks and branchs are automatically created at adoption or later:
    * When feature or refacto task DoR is ok and adopted in daily:
      * **poc/*RUID*-x** subtask & branch is created if needed (info is in task).
      * **docs/*RUID*-x** subtask & branch is created when feature task DoR is ok.
    * When technical documentation is validated by the MA:
      * **feature/*RUID*-x** branch is created for feature.
      * **refactor/*RUID*-x** branch is created for a refacto.
    * Conflict subtask & branch might be created at merge by the MA.
      * **conflict/*RUID*-x_*RUID*-y** the both task teams are responsible for resolution. 
    * If the RUID is the in test automation list
      * **test/*RUID*-x** subtask & branch is created.
    * If the PO identify a bug, or get an issue from QA or hotfix is asked by the exploitation :
      * **fix/*RUID*-x** subtask & branch is created (By default the task goes to the mini team who is responsible for the feature).
    * If the RUID is the in the hardening list
      * **security/*RUID*-x** subtask & branch is created and attribued to devSec experts
  * Verifiy the develop branch is always globally functional and allow to start developments.
  * with POC :
    * POC on **poc/*RUID*-x** subtask & branch from develop (automatically created at adoption).
    * Validate the poc with the PO and the Maintainer.
    * Estimate task difficulty, risk level and time.
  * Add an additional unit test and valid it with the PO.
  * Make technical specifications on **docs/*RUID*-x** subtask & branch from develop .
    * Make technical specifications for his features, refactor or big fix.
    * Identify related general technical specification, get recos from the maintainer.
    * Identify code perimeter :
      * Gitblame to find previous developers on this code section, talk with them about it.
      * Add impacted code perimeter information to the task.
      * Check at daily if others tasks may create any conflicts.
        * Ask maintainer for a tactic to avoid doublon or conflicts.
    * Validate his technical specifications and docs with the maintainer.
    * Ask for test fixtures or create them.
    * Explain his tech spec to the dev-team.
  * Creates **feature/*RUID*-x** branch from develop.
    * Develop the feature.
    * Pass the unit tests in a dev-test env automaticly deployed.
    * May update the feature branch, but only if it doesn't impact your code.
  * Ask PO validation for his automated deployed feature.
    * Open new task if the fonctional spec is changed, re-check DoR, re-estimate.
  * Ask the maintainer for code review.
    * Make needed changes.
    * Pass all the tests.
    * Ask the maintainer for code review.
    * If code is OK, branch is tagged OK_feat_*RUID*-x, the feature task is finished.
    * (The maintainer check updates and merge potentials conflicts)
  * If **conflict/*RUID*-x_*RUID*-y** subtask have been created by the maintainer:
    * corresponding **conflict/*RUID*-x_*RUID*-y** branch have been created.
    * gitblame identify who will participate to this task.
    * estimate conflict resolution the task.
    * resolve the conflicts.
    * Pass the all the tests.
    * Ask the maintainer for code review.
    * If code is OK, branch is tagged OK_*RUID*-x_*RUID*-y, the conflict task is finished.
    * (The maintainer check updates and merge)
* If test automation is required :
  * **test/*RUID*-x** automation unit test subtask is created.
  * **test/*RUID*-x** branch is created.
  * May ask QA for advices or help.
  * May ask GitOps for help.
  * Develop the tests and organise needed fixtures.
  * Ask QA for automated test review.
  * Ask PO for automated test review.
  * Ask the maintainer for code review.
  * If OK, branch is tagged OK_test_*RUID*-x, the test task is finished.
  * (The maintainer check updates and merge potentials conflicts)
* If fix **fix/*RUID*-x** subtask is created by the PO :
  * **fix/*RUID*-x** branch is created.
  * May ask PO, QA or MA for advices or help.
  * Fix it
  * Ask PO validation for his automated deployed feature, if not trivial.
  * Ask the maintainer for code review.
  * If OK, branch is tagged OK_fix_*RUID*-x, the fix task is finished.
  * (The maintainer check updates and merge potentials conflicts)
* If performance optimizations, dependencies updates are needed some **perf/*RUID*-x** or **chlore/*RUID*-x** tasks and branchs might be created.

### **GitOps** - **G**it**O**ps:

DevOps using gitlab, advocate and implement best parctices. 

* **Best practices advocates.**
* Help maintainer.
* Help developers for test automation.
* Help QA for test env. and automation.
* Make IPD cosy with the maintainer.
* Help setting cyber security inside the CI/CD pipelines.
* Communicate with DevOps, Infra et security teams.
* CI/CD on **ci/*RUID*-x** task & branch from develop (automatically created at adoption).
* dependabot/ renovate/ tasks observator and responsible

### **AgileMonk** - **A**gile **M**onk:

As Master is a term that is abandonned in branch naming, it should be avoid as role naming.
In a team "Master" or "SM" sado mazo initials may attrack sadists or psycopaths.
The flaccid scrum master is a sample of dramatic miss understanding of agile philosophy.
Monk is better for the ego of an agile consultant.
The Monk Agile, is a team builder and team protector, it ensure the cosy spirit needed for best realisations.

* **The Agile monk conducts the ceremonies**:
  * **Matins** With the POMO, the QAAT and the TAM.
    * Back Log:
      * Review Requirements and details specifications with the POMO and TAM ready for refinements.
      * Review Tasks Priorities.
    * Plan next **Refinement ceremony** with DEX or GitOps.
    * Prepare external ceremonies with third party linked to the project (demo, presentation).
  * The **Prime**: Prepare the **Daily ceremony** update tasks status, prepare questions, check pipelines.
  * The **Tierce Daily ceremony** with DEX, DevOps, QAAT, POMO, TAM.
  * The **None ceremony** : ensure none conflicts, blurs, resources need or blocking situations.
  * The **CRC & refinement**, **planning poker** and **retro** **sprint** ceremonies.  
* Ensure there is **no blame culture**.
* **Agility Best Practices Advocate.**
  * Help for DoR, DoD and ceremony cycle elaboration.
* **Test Driven** Advocate.
* **KISS Advocate** :
  * Check miss understandings.
  * Ensure the main Jalons & MileStones are clear.
  * Check task granularity.
  * Check task quality.
  * Check IPD and workflows are clear for each developer.
  * Check specifications are clear for each developer.
  * Check task boards is simple.
* CNV & Palo Alto practice lead.
* **Team protector**:
  * Team building.
  * Team needs identification, advocacy, resolution.
  * Check specifications are ready before realisation.
  * Check if IPD is cosy for the developers.
  * Verify time estimation is done freely.
  * Verify tasks adoption id done by the developers.
  * Verify feature specifications are not changed after DoR is valided.
  * Verify feature tasks are not added to the sprint after is started.
  * Verifiy unit tests and acceptance tests are not modified during the sprint.
  * Verifiy the develop branch is always globally functional and allow to start developments.
  * Valorise teams work.
  * Avoid chaos, psychopathy & standford lucifer effects.
* **Tasks management** :
  * Check, update tasks status.
    * Check if help or resources are needed.
    * Look for help or resources if asked.
  * Update the tasks boards.
  * Make task boards cosy.
  * Make summary notes.
  * Velocity estimation.
  
## Git Branchs

* nomenclature : modification type / requirement-uid or version
  * ruid - requirement-uid github regexp : `[A-Z]+-[A-Z]+-[A-Z]+-[a-z]?[0-9]+`
  * version - release version number github regexp : `[0-9]+.[0-9]+.[0-9]+`
* environements :
  * DEV : localhost, on the developper host or development dedicated private environement (vm, remote server..).
  * DEMO : team remote host (vm, k8s service, servers) automated deployement of a feature for démo and unit validation.
  * QA : team remote host automated deployement of integration develop branch or alpha release for acceptance tests and demo.
  * PPD : team remote host automated deployement of future release branch for pre production system tests.
  * PROD : public remote host automated deployement for production.

| nomenclature  | usage | source branch | target branch | environments |
|-------------- |-------|---------------|---------------|--------------|
| poc/ruid      | Proof of concept for a new feature faisability exploration | develop | squash and keeped | DEV, DEMO |
| docs/ruid     | Technical documentation    | develop | develop | DEV, DEMO |
| feature/ruid  | New feature development    | develop | develop | DEV, DEMO |
| fix/ruid      | feature fix development    | develop | develop | DEV, DEMO |
| refacto/ruid  | refactoring (iso functionalities) | develop | develop | DEV, DEMO |
| security/ruid | security hardening of code | develop | develop | DEV, DEMO |
| ci/ruid       | CI/CD developments         | develop | develop | DEV, DEMO, QA, PPD |
| test/ruid     | tests automation           | develop | develop | DEV, DEMO |
| dependabot/*  | Bot automated dependencies updates | develop | develop | DEV, DEMO |
| renovate/*    | Bot automated project source updates | develop | develop | DEV, DEMO |
| perf/ruid     | Performance optimization   | develop | develop | DEV, DEMO, PPD |
| chlore/uid    | dependencies updates       | develop | develop | DEV, DEMO |
| develop       | Integration branch, check all development works after merge | features, fix, docs, refactos.. | release/alpha | QA |
| release/alpha | QA acceptance tests for release | release/alpha | security/version  | QA |
| security/version | automated security hardening of code blocking developments or unit tests | security/version | release/version | QA, PPD |
| release/version  | Maintainer System Tests | security/version | release/version | PPD  |
| main             | production branch       | release/version | main + version tag |  PROD |
| hotfix/ruid      | Hot fix of blocking bug in production | main | release/version and main + version tag | PPD |
| *wip*            | Work in progress |  develop | develop | DEV |