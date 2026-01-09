# ${{values.name}}

- [${{values.name}}](#valuesname)
  - [${{values.uid}}](#valuesuid)
  - [Application documentation](#application-documentation)
  - [Zen Programmin (ZP)](#zen-programmin-zp)
    - [Cycle](#cycle)
    - [Attitude](#attitude)
    - [Strategy](#strategy)
    - [Tactics](#tactics)
  - [**TAZ** -  **T**eam **A**gile **Z**en](#taz----team-agile-zen)
    - [**POMO** - **P**roduct **O**wner \& **M**ilestones **O**rchestrator:](#pomo---product-owner--milestones-orchestrator)
    - [**QAAT** - **Q**uality **A**ssement \& **A**cceptance **T**ests:](#qaat---quality-assement--acceptance-tests)
    - [**TAM** - **Technical**  **A**rchitect \& **M**aintainer:](#tam---technical--architect--maintainer)
    - [**DEX** - **D**evelopers **EX**perts:](#dex---developers-experts)
    - [**GitOps** - **G**it **O**ps:](#gitops---git-ops)
    - [**SecOps** - **S**ecurity **O**ps:](#secops---security-ops)
    - [**AgileMonk** - **A**gile **M**onk:](#agilemonk---agile-monk)
  - [Environments](#environments)
  - [Git Branchs](#git-branchs)
  - [**General Functional Specifications:**](#general-functional-specifications)
  - [**Technical Response**](#technical-response)
    - [**General Technical Requirements**.](#general-technical-requirements)
    - [**Main Epics**.](#main-epics)
    - [**Technical choices strategy, tactic and criterias**.](#technical-choices-strategy-tactic-and-criterias)
    - [**Main technical bedrock : tools and instruments choices**.](#main-technical-bedrock--tools-and-instruments-choices)
    - [**General Technical Specifications**.](#general-technical-specifications)
  - [**Main Milestones**](#main-milestones)
  - [DoR (Definition of Ready)](#dor-definition-of-ready)
  - [DoD (Definition of Done)](#dod-definition-of-done)

## ${{values.uid}}

- deployment environements : ${{values.environements}}
- owner: ${{values.owner}}

## Application documentation

[DOC](docs/index.md)

## Zen Programmin (ZP)

**TAZ** -  **T**eam **A**gile **Z**en:

* [Developer & Experts team](#dex---developers-experts)
* [Product Owner MileStones Ochestrator](#pomo---product-owner-milestones-orchestrator)
* [Technical Architect & Maintainer ](#tam---technical--architect--maintainer)
* [Quality & Acceptance Tests Team](#qaat---quality-assement-acceptance-tests)
* [Agile Monk](#agilemonk---agile-monk)

### Cycle

1. **Gestation**
   1. POMO & TAM
      1. **Business Glossary & Acronyms** creation.
      2. **General Fonctional Requirements** overview and **Main Epics** identification.
      3. **Cosy IDP** bedrock with gitOps best practices.
      4. [**General Functional Specifications:**](#general-functional-specifications)<details><summary>Actors, Use Cases, CRC, Workflows</summary>[General Functional Specifications Details](#general-functional-specifications)</details>
      5. [**Technical Response**](#technical-response)<details><summary>General Requirements, Epics, Choices & Specification</summary>[Technical Response Details](#technical-response)</details>  
      6. **Requirements Prioritization & Risk estimation**
2. **Week Iterations** :
   1. **Monday, tuesday, wednesday, thursday**:
         1. DEX, POMO, TAM :
            1. Tierce **Daily Ceremonies** with Cosy Communication.
            2. **Continuous Task Validation & Delivery** in user story (US) environement demonstration (DEMO).
         2. QAAT :
            1. **Continuous acceptance testing** (AT) in qualification (QAL) environment (of develop integration branch).
   2. **Thursday Release validation & publication phase**:
      1. DEX : 
         1. **Code cleanning**: refactoring, dependencies updates, security, perf, doc amelioration (of develop integration branch).
      2. QAAT : 
         1. **Alpha-release acceptance testing** (AT) in AT pre-production (PPD) environment.
      3. TAM : 
         1. **Alpha-release system testing** (ST) in ST pre-production (PPD) environment .
         2. **Release publication in producton** (PROD) environment.
   3. **Friday**
      1. DEX, TAM & QAAT:
         1. **Cleaned Code Validation**
      2. POMO:
         1. **User Stories (US) definition** & CRC (Class, Responsibility, Collaborator) & **raffinement**.
         2. **Tasks Redaction, Prioritization & Risk estimation**.
      3. DEX, POMO, TAM:
         1. Realistic Developer-EXperts (DEX) - pocker planning - **Task time estimation**.
      4. The whole team:
         1. **Retro & Team work valorization**


### Attitude

1. Respectful
2. Thoughtfulness
3. Undertaking
4. Positive
5. Quiet strength
6. Pragmatic
7. Realist

### Strategy

Think first, discuss, specify, try, adapt, deliver then simplify and document.

### Tactics

1. Auto organisation of developpers and experts for duo or trio programming.
2. Repetitive task automation.
3. One source of truth in one documentation.
4. Simple and clear, not fuzzy, not duplicated specification.
5. Test, try and refine.
6. Don't blame, help, keep things simple and be clear.
7. Ask and give feed backs quickly.

## **TAZ** -  **T**eam **A**gile **Z**en

| | | | | | | |
|---|---|---|---|---|---|---|
| [**POMO**](#pomo---product-owner-milestones-orchestrator) | [**QAAT**](#qaat---quality-assement-acceptance-tests) | [**TAM**](#tam---technical--architect--maintainer) | [**DEX**](#dex---developers-experts) | [**GitOps**](#gitops---gitops) | [**SecOps**](#secops---secops) | [**AgileMonk**](#agilemonk---agile-monk) |

### **POMO** - **P**roduct **O**wner & **M**ilestones **O**rchestrator:

Final Product Responsable - **Decide how the product must work for final users**.
Supervise functional requirements, specification redaction and features tasks redaction.
Schedule and orchestrate the project advancement.
Validate functional tasks understanding and implementation.

<details><summary>responsabilities</summary>

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
  * Give the GO for **alpha release** with the QAAT (after QAAT has done acceptance tests).
  * Give the GO for **MEP** with the maintainer (after maintainer systems tests in PPD).
  * Ask MEP potential rollback.
  * Give the GO for **QAAT test** strategy, tactics and acceptance test plans.
  * Give the GO for **test automation** strategy, tactics and tasks.
  * Give the GO for **refactoring** strategy, tactics and tasks.

</details>

### **QAAT** - **Q**uality **A**ssement & **A**cceptance **T**ests:

Quality Accessment and Acceptance tests responsables - Validate applications are working and respects specifications.

<details><summary>responsabilities</summary>

* Participate to the **functional testing automation** strategy and tactics with the maintainer.
* Responsible for **acceptance tests** strategy, tactics and plan.
* **Manage Acceptance Tests Epics and Milestones.**
* **Blur hunting** :
  * Ask details and explanations about specifications.
  * Ask glossary term clarification, disambiguation and deduplication.
* Ask fixtures for testing.
* Validate acceptance testing plan with PO.
* Make Acceptance tests (with requirements uid) in QAL integration env.
* **Validate** the integration develop branch (alpha release).
* Open bug issues with the PO.
* Give the **GO for alpha release** with the PO.
* Create test automation tasks.
* Share their automated tests with the dev-team (shifleft).
  
</details>

### **TAM** - **Technical**  **A**rchitect & **M**aintainer:

Technical Maintainer & Architect who lead the tech teams. Supervise good pratices enforcement and IDP improvements.
Decide for the global technical architectures and support technical teams for specifications and implementation.
Supervise deployments automation in Feature Demo, QAL, PPD and MEP environements.
Manage code reviews, code update, merge request, merges and conflicts.

*The merge conflicts might be a source of chaotic behaviours, the dev-team must be protected from conflicts. The mini-task-teams work evaluation must not be impacted by code conflicts. If work evaluation was impacted, it would permit conflict makers to look faster and more efficients than impacted ones.*

<details><summary>responsabilities</summary>

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
  * Help QAAT to get adapted fixtures and cosy testing environements.
  * Help PO, participate to DoR and DoD with the dev-team.
* **IDP Responsable** :
  * Set & check technical constraints.
  * GitOps or GitOps main contact.
  * Keep Internal Development Plateform cosy.
* **Technical Tasks Redaction** :
  * Validate the DoR and DoD with all the dev-team.
  * Create **tech-spec/*RUID*-x** technical specification tasks.
    * Feature description :
      * Requirement uid selection should add :
        * Ref & Link to RUID. 
        * Related general specification version, chapter, section and **user story** link.
        * Tests list and links.
      * some fixtures and an example.
    * Ensure the developers got a good understanding of the new features.
    * Ensure there is no task duplicatas.
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
  * Do or Supervise the MEP with the POMO GO.
* **Hotfix**
  * **hotfix/*RUID*-x** branch might be created from the main branch by the POMO (from hotfix subtask creation).
  * The maintainer supervise or resolve the hotfix and hot related MEP.
  * The corresponding fix task branch have been created from develop branch.
* **TDD Lead**
  * Set the unit testing automation strategy and tactics with the dev-team.
  * Set the functional testing automation strategy and tactics with the QAAT.
  * Set the testing priority with the POMO and the QAAT.
  * Keep requirements test automation list.
  * Creates automation testing tasks.
* **Refactoring Lead**
  * Creates refactoring strategy and tactics.
  * Validate refactoring strategy, tactics and priorities with the dev-team and PO.
  * Create refactor tasks.
* If CI/CD, performance optimizations or dependencies updates are needed some **ci/*RUID*-x** **perf/*RUID*-x** or **chlore/*RUID*-x** tasks and branchs might be created by the MA.
  
</details>

### **DEX** - **D**evelopers **EX**perts:

Developers and technical experts, responsable for their features technical specification and implementation.
Validate specification redaction respect DoR.
Participate to the DoR and DoD elabration. Source of proposals for IDP, tasks board improvements and technologies choices.
Auto-organise in duo or trio mini task teams.

<details><summary>responsabilities</summary>

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
    * If the POMO identify a bug, or get an issue from QAAT or hotfix is asked by the exploitation :
      * **fix/*RUID*-x** subtask & branch is created (By default the task goes to the mini team who is responsible for the feature).
    * If the RUID is the in the hardening list
      * **security/*RUID*-x** subtask & branch is created and attribued to devSec experts
  * Verifiy the develop branch is always globally functional and allow to start developments.
  * with POC :
    * POC on **poc/*RUID*-x** subtask & branch from develop (automatically created at adoption).
    * Validate the poc with the POMO and the Maintainer.
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
  * Ask POMO validation for his automated deployed feature.
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
  * May ask QAAT for advices or help.
  * May ask GitOps for help.
  * Develop the tests and organise needed fixtures.
  * Ask QAAT for automated test review.
  * Ask POMO for automated test review.
  * Ask the maintainer for code review.
  * If OK, branch is tagged OK_test_*RUID*-x, the test task is finished.
  * (The maintainer check updates and merge potentials conflicts)
* If fix **fix/*RUID*-x** subtask is created by the POMO :
  * **fix/*RUID*-x** branch is created.
  * May ask PO, QAAT or MA for advices or help.
  * Fix it
  * Ask POMO validation for his automated deployed feature, if not trivial.
  * Ask the maintainer for code review.
  * If OK, branch is tagged OK_fix_*RUID*-x, the fix task is finished.
  * (The maintainer check updates and merge potentials conflicts)
* If performance optimizations, dependencies updates are needed some **perf/*RUID*-x** or **chlore/*RUID*-x** tasks and branchs might be created.

</details>

### **GitOps** - **G**it **O**ps:

DevOps using gitlab, advocate and implement best practices.

<details><summary>responsabilities</summary>

* **Best practices advocates.**
* Help maintainer for gitOps.
* Help developers for test automation.
* Help QAAT for test env. and automation.
* Make IPD cosy with the maintainer.
* Help setting cyber security inside the CI/CD pipelines.
* Communicate with DevOps, Infra et security teams.
* CI/CD on **ci/*RUID*-x** task & branch from develop (automatically created at adoption).
* dependabot/ renovate/ tasks observator and responsible

</details>

### **SecOps** - **S**ecurity **O**ps:

SecOps advocate and implement best security practices.

<details><summary>responsabilities</summary>

* **Best security practices advocates.**
* Help maintainer for security.
* Help developers for security test automation.
* Help QAAT for security test env. and automation.
* Make IPD secure with the maintainer.
* Help setting cyber security inside the CI/CD pipelines.
* Communicate with GitOps, DevOps, Infra et security teams.
* CI/CD on **secu/*RUID*-x** task & branch from develop (automatically created at adoption).
* dependabot/ renovate/ tasks observator and security responsible

</details>

### **AgileMonk** - **A**gile **M**onk:

As Master is a term that is abandonned in branch naming, it should be avoid as role naming.
In a team "Master" or "SM" sado mazo initials may attrack sadists or psycopaths.
The flaccid scrum master is a sample of dramatic miss understanding of agile philosophy.
Monk is better for the ego of an agile consultant.
The Monk Agile, is a team builder and team protector, it ensure the cosy spirit needed for best realisations.

<details><summary>responsabilities</summary>

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
  * Team needs identification, advocacy and resolution.
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
  
</details>

## Environments

DEV > DEMO > QALIF > PPD > PROD

* **DEV** : localhost, on the developper host or development dedicated private environement (vm, remote server..).
* **DEMO** : team remote host (vm, k8s service, servers) automated deployement of a feature for démo and unit validation.
* **QALL** : team remote host automated deployement of integration develop branch or alpha release for acceptance tests and demo.
* **PPD** : team remote host automated deployement of future release branch for pre production system tests.
* **PROD** : public remote host automated deployement for production.

## Git Branchs

* nomenclature : modification type / requirement-uid or version
  * ruid - requirement-uid github regexp : `[A-Z]+-[A-Z]+-[A-Z]+-[a-z]?[0-9]+`
  * version - release version number github regexp : `[0-9]+.[0-9]+.[0-9]+`

| nomenclature  | usage | source branch | target branch | environments |
|-------------- |-------|---------------|---------------|--------------|
| poc/ruid      | Proof of concept for a new feature faisability exploration | develop | squash and keeped | DEV, DEMO |
| docs/ruid     | Technical documentation    | develop | develop | DEV, DEMO |
| feature/ruid  | New feature development    | develop | develop | DEV, DEMO |
| fix/ruid      | feature fix development    | develop | develop | DEV, DEMO |
| refacto/ruid  | refactoring (iso functionalities) | develop | develop | DEV, DEMO |
| security/ruid | security hardening of code | develop, release/alpha | develop | DEV, DEMO, QAL |
| perf/ruid     | Performance optimization   | develop, release | develop | DEV, DEMO, QAL |
| ci/ruid       | CI/CD developments         | develop | develop | DEV, DEMO, QAL |
| test/ruid     | tests automation           | develop | develop | DEV, DEMO |
| dependabot/*  | Bot automated dependencies updates | develop | develop | DEV, DEMO |
| renovate/*    | Bot automated project source updates | develop | develop | DEV, DEMO |
| chlore/uid    | dependencies updates       | develop | develop | DEV, DEMO |
| develop       | Integration branch, check all development works after merge | features, fix, docs, refactos.. | release/alpha | QAL |
| release/alpha | QAL acceptance tests for release | release/alpha | security/version  | QAL |
| security/version | automated security hard. of code | security/version | release/version | QAL, PPD |
| perf/version     | automated performance opti. of code | perf/version  | release/version | QAL, PPD |
| release/version  | Maintainer System Tests | security/version | release/version | PPD  |
| main             | production branch       | release/version | main + version tag |  PROD |
| hotfix/ruid      | Hot fix of blocking bug in production | main | release/version and main + version tag | PPD |
| *wip*            | Work in progress |  develop | develop | DEV |

*some optimisation or security patch, may be not so practicle for development or unit tests (slow or complicated). So they are applied automaticly for acceptance and system testing*

## **General Functional Specifications:**
 
 <summary>Actors, Use Cases, CRC, Workflows:</summary>
 
1. Business **Roles** & **Entities**.
2. **Use Cases** diagrams and description.
3. **Story boards**.
4. **CRC** (Class, Responsibility, Collaborator) & **Sequence** diagrams.


## **Technical Response**

<summary>General Requirements, Epics, Choices & Specification:</summary>

### **General Technical Requirements**.

### **Main Epics**.

The main epics will identifiy main subjects/parts of the final product.

<details><summary>For an online shop, epics could be like this :</summary>

* MODEL
  * MODEL-USER
  * MODEL-CATALOG
  * MODEL-ARTICLE
  * MODEL-STOCK
  * MODEL-VENDOR
  * MODEL-CLIENT
  * MODEL-CMD
  * MODEL-TRSPT
* APIREST
  * APIREST-USER
  * APIREST-CATALOG
  * APIREST-ARTICLE
  * APIREST-STOCK
  * APIREST-VENDOR
  * APIREST-CLIENT
  * APIREST-CMD
  * APIREST-TRSPT
* BACK
  * BACK-USER
  * BACK-LOGIN
  * BACK-CATALOG
  * BACK-ARTICLE
  * BACK-STOCK
  * BACK-VENDOR
  * BACK-CLIENT
  * BACK-CMD
  * BACK-TRSPT
* FRONT
  * FRONT-LOGIN
  * FRONT-CUSTOMER-CART
  * FRONT-ARTICLE-VIEW
  * FRONT-ARTICLES-LIST
  * FRONT-CUSTOMER-CMD
</summary>

### **Technical choices strategy, tactic and criterias**.

<summary>sample of basic criterias:</summary>

1. Licence.
2. Size of community.
3. Recent Activity.
4. Code Quality, security & best practices.
5. Referenced by a fundation.
6. Easy to use.
7.  Efficiency.
   
### **Main technical bedrock : tools and instruments choices**.

<details><summary>Langages, Frameworks, Data management, testing tools, hosts, measure instruments:</summary>

1.  Programming **Langages** (PHP, Python, Java, Go, Rust, PlPGSQL, NoSQL, ECMAScript, TypeScript...).
2.  **Frameworks** (Symfony, Django, Spring, Gin, Actix, NodeJS; VueJS, React, Angular...).
3.  CMS, Applications, Librairies...
4.  **Dependencies**, packet manager tools.
5.  **Data management tools** (Databases, Brokers, Data Lakes ...)
6.  **Hosting** (on promise, cloud, vm or container, os...)
7.  **Testing tools** (Selenium, Fitness, Datadog, JMeter, Acunetix, Postman; Jest, Mocha, Cypress...)
8.  **Linters, Code Quality Instruments** (SonarQube, Checkmarx...)
</details>

### **General Technical Specifications**.

<details><summary>Entities, Use Cases, CRC, Workflows, Best Pratices:</summary>

1.  Technical  **Roles** & **Entities**.
2.  **Use Cases** diagrams and description.
3.  **Components** diagrams and description.
4.  **CRC** (Class, Responsibility, Collaborator) & **Sequence** diagrams.
5.  **States** diagrams and description.
6.  **Containerisation** or **virtualisation**.
7.  **Mocking & delivery strategies and tactics**.
8.  **Delivery workflows, dependencies managment**.
9.  **Best Practices docs**.
</details>

## **Main Milestones**

The milestone will fix goals, for exemple : having specifications, good work environement, technical bed rock with chooseen frameworks, application base with authentication and user management, first poc, first demo, version 1 with a minimal functional permimeter...

<details><summary>The milestone acronyms might loook like : </summary>
1. idp_base
2. spec_base
3. survey_inst
4. mrktg_pres
5. app_base
6. app_poc
7. mrktg_com
8. app_demo
9. app_v1
10. app_v2
</details>

## DoR (Definition of Ready)

The DoR will list all the requirements to considere task faisable & ready for development.
The wall team must agree on a task DoR. The team and in particular de DEX teams should verify DoR prerequisites before any time, difficulty, risk of effort estimation.
The DoR will fix all the elements that any kind of task need to have, before it is ready for implementation.
If their is blur in specification, usually the blame goes to the developper or expert who took the task. That is unfair and demotivate the DEX teams.

<details><summary>A DoR, could be:</summary>

* Feature description is complete :
  * Requirement & Specifications must be ready.
  * Requirement uid selection should add :
    * Ref & Link to RUID. 
    * Related general specification version, chapter, section and **user story** link.
    * Tests list and links.
  * some fixtures and an example.
  * there is no duplicatas
  * resourses needed are accessible.
* Ensure the developers got a good understanding of the new features.
* Ensure there is no task duplicatas.
* Estimate the difficulty level have been done by the DEX team & TAM.
* Estimate the risks:
  * New technology surprises.
  * Dependencies to third parts.
  * ...
* Time and effort estimation have been done by the DEX team.
* We have identifed and communicated about the impacted code areas.
</details>


## DoD (Definition of Done)

The DoD we list all the requirements to set status at done.
The wall team must agree on a task DoD. Each type of task should have an adapted DoD.
The Merge Request and Merge and non regression on the develop branch could be asked for feature tasks.
If you want to avoid a situation where quick and dirty merges give more benefits to quick and dirty developments and disavantage the rest of the team; you may prefere decorrelation between the feature or fix developement and its merge.
The develop integration branch must be clean and working all sprint long.
The feature realisation is judged without external updates.
Conflicts resolution should not impact performance evaluation.
Complex and clean developments can takes longer, the last who merge should not be the looser of the team.
Conflicts resolution might be complex, in this context, amha it shoud be a separated task.

<details><summary>One flow disgression</summary>
On a oneflow with well decoupled microservices or alone, we may avoid conflicts by attributing code area responsablities. In this case, you might probalbly avoid many subtasks management and the DoD of features, fix, refacto may englob many many steps : Doc, Unit tests automation, Update before Merge Request and Non regression verification, passing all automated tests and quality code, code cleaning, security enforment, performance optimization...
</details>

<details><summary>A feature development task DoD in a monolitic Application with a big team, could be :</summary>

1. The TAM is ok for technical specification.
2. The feature codding started from updated develop branch.
3. The PO is ok for the implementation functional result.
4. The TAM is ok for the technical implementation and code documentation.
5. With no further updates from develop, it is passing all the non regression tests.

The TAM, merge the branch in develop and may open distinct tasks.
</details>

* Fix tasks might not need the technical specification step.
* Refacto might need a risk evaluation step, or timing constraint and more testing.
* Conflict DoD might include the validation of all implicated or impacted developpers.
