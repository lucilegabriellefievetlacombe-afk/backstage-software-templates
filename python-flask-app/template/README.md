# ${{values.name}}

- [${{values.name}}](#valuesname)
  - [${{values.uid}}](#valuesuid)
  - [Application documentation](#application-documentation)
  - [**TAZ** -  **T**eam **A**gile **Z**en](#taz----team-agile-zen)
    - [**POZ** - **P**roduct **O**wner **Z**en:](#poz---product-owner-zen)
    - [**QAZ** - **Q**uality **A**ssement **Z**en:](#qaz---quality-assement-zen)
    - [**MAZ** - **M**aintainer **A**rchitect **Z**en:](#maz---maintainer-architect-zen)
    - [**DEZ** - **D**evelopers **E**xpert **Z**en:](#dez---developers-expert-zen)
    - [**GOZ** **G**it**O**ps **Z**en:](#goz-gitops-zen)
    - [**MAZ** - **M**onk **A**gile **Z**en:](#maz---monk-agile-zen)

## ${{values.uid}}

- deployment environements : ${{values.environements}}
- owner: ${{values.owner}}

## Application documentation

[DOC](docs/index.md)

## **TAZ** -  **T**eam **A**gile **Z**en

[**POZ** - **P**roduct **O**wner **Z**en](#poz---product-owner-zen) |
[**QAZ** - **Q**uality **A**ssement **Z**en](#qaz---quality-assement-zen) |
[**MAZ** - **M**aintainer **A**rchitect **Z**en](#maz---maintainer-architect-zen) |
[**DEZ** - **D**evelopers **E**xpert **Z**en](#dez---developers-expert-zen) |
[**GOZ** **G**it**O**ps **Z**en](#goz-gitops-zen) |
[**MAZ** - **M**onk **A**gile **Z**en](#maz---monk-agile-zen)

### **POZ** - **P**roduct **O**wner **Z**en:

Final Product Responsable - **Decide how the product must work for final users**.
Supervise functional requirements, specification redaction and features tasks redaction.
Schedule and orchestrate the project advancement.
Validate functional tasks understanding and implementation.

* **Functional Specifications Redaction** :
  * Responsable for general functional specifications.
  * Responsable for detailed functional specifications.
  * Take in account technical specification constraints and requirements.
* **Manage Requirements** :
  * Organise functionnal requirements :
    * Requirement UID - **RUID**
      * UID nomenclature is linked to epics or specification and milestones in a way that does not creates doublon and faciltate understanding : ex BACK-LOGIN-ADMIN, FRONT-LOGIN-USER, BACK-ADD-CATALOG-ARTICLE, BACK-ADD-ARTICLE-IDENTIFICATION, BACK-ADD-ARTICLE-STOCK, FRONT-CUSTOMER-CART, FRONT-ARTICLE-VIEW, FRONT-ARTICLES-LIST.
    * Theme.
    * Related Epics.
    * Description.
    * Related general or detailed specification version, chapter and section.
    * Priority.
    * Risk.
    * Related MileStones.
    * Code Avancement.
    * Test coverage.
    * Automated test coverage.
  * Follow all requirements advancement.
* **Fonctional Tasks Redaction** :
  * Validate the DoR and DoD with the Maintainer and the dev-team.
  * Create **func-spec_*RUID*-x** functional specification tasks.
    * Feature description :
      * Related general specification version, chapter and section.
      * Requirement uid.
      * context : pages, user roles, action, entities, status-step-event.
      * what action ?
      * what result ?
      * how to test it is working ?
      * fixtures and an example.
    * Ensure the developers got a good understanding of the new features.
    * Ensure there is no task doublons.
    * Ensure features are linked with an exigence.
* **Manage Fonctional Epics and Milestones** (taking in account technicals necessities).
* **Feature Fonctional Unit Tests & Validation**.
* Create **fix_*RUID*-x** **fix** or **hotfix** tasks.
  * describe the bug or refining for **func-spec_*RUID*-x**.
  * if needed add additional tests.
  * if it is blocking the production :
    * add label hotfix to the task.
    * ping and assign any hotfix to the maintainer.
* **Orchestration** :
  * Give the GO to the next **Milestone**.
  * Give the GO for the new **Sprint**.
  * Give the GO for **features POC or development tasks** (after DoR ok).
  * Give the GO for **features code review** (after functional unit testing).
  * Give the GO for **alpha release** with the QA (after QA has done acceptance tests).
  * Give the GO for **MEP** with the maintainer (after maintainer systems tests in PPD).
  * Ask MEP potential rollback.
  * Give the GO for **QA test** strategy, tactics and acceptance test plans.
  * Give the GO for **test automation** strategy, tactics and tasks.
  * Give the GO for **refactoring** strategy, tactics and tasks.

### **QAZ** - **Q**uality **A**ssement **Z**en:

QA Acceptance tests responsables - Validate applications are working and respects specifications.

* Participate to the **functional testing automation** strategy and tactics with the maintainer.
* Responsible for **acceptance tests** strategy, tactics and plan.
* **Manage Acceptance Tests Epics and Milestones.**
* **Blur hunting** :
  * Ask details and explanations about specifications.
  * Ask glossary term clarification.
* Ask fixtures for testing.
* Validate acceptance testing plan with PO.
* Make Acceptance tests (with requirements uid) in QA integration env.
* **Validate** the integration develop branch (alpha release).
* Open bug issues with the PO.
* Give the **GO for alpha release** with the PO.
* Create test automation tasks.
* Share their automated tests with the dev-team (shifleft).
  
### **MAZ** - **M**aintainer **A**rchitect **Z**en:

Maintainer & Architecte lead the tech teams. Supervise good pratices enforcement, IDP improvements.
Decide for the global technical architectures and support technical teams for specifications and implementation.
Manage features code reviews, merges and conflicts.
Supervise deployments automation in Feature Demo, QA, PPD and MEP environements.

* **Best technical pratices advocate**.
* **Lead the global technical specifications**.
  * Validate features technical specifications.
  * Anticipate and manage code conflicts or doublons.
* **Manage Technical Epics and Milestones.**
* **Organise technical requirements (according to functional needs)** :
  * Requirement UID - **RUID**
    * UID nomenclature is linked to epics or specification and milestones in a way that does not creates doublon and faciltate understanding : ex AUTH-ADMIN, AUTH-CUSTOMER, LOG-USER-ACTIONS, LOG-CATALOG-EVENTS, LOG-ARTICLE-STOCK...
  * Theme.
  * Related Epics (all).
  * Description.
  * Related tecnical specification version, chapter and section.
  * Priority.
  * Risk.
  * Related Milestones (all).
  * Code Avancement.
  * Test coverage.
  * Automated test coverage.
  * Follow technical requirements advancement.
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
        * **conflict_*RUID*-x_*RUID*-y** subtask and branch is created
        * gitblame tel who will participate to this task
* **Relases Deployment & MEP**
  * Do or supervise creation and deployment of the alpha release branchs.
  * Do or supervise creation and deployment of the latest releases in PPD.
  * Do or Supervise system tests before MEP.
  * Do or Supervise the MEP with the PO GO.
* **TDD Lead**
  * Set the unit testing automation strategy and tactics with the dev-team.
  * Set the functional testing automation strategy and tactics with the QA.
  * Set the testing priority with the PO and the QA.
  * Keep requirements test automation list.
  * Creates automation testing tasks.
* **Refacto Lead**
  * Creates refactoring strategy and tactics.
  * Validate refactoring strategy, tactics and priorities with the dev-team and PO.
  * Create refacto tasks.
  
### **DEZ** - **D**evelopers **E**xpert **Z**en:

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
* Adopt a feature alone, or in a duo or trio mini team.
  * Auto-organise RASIC for duo/pair or trinome/trio task team.
  * Task and subtasks and branchs are automatically created at adoption or later :
    * **poc_*RUID*-x** subtask & branch is created if needed (info is in task).
    * **tech-spec_*RUID*-x** subtask & branch is created.
    * **feature_*RUID*-x** branch is created.
    * *conflict_*RUID*-x_*RUID*-y* subtask & branch might be created at merge.
    * **auto-ut_*RUID*-x** subtask & branch is created if needed (info is in requirements automation list).
    * *fix_*RUID*-x* subtask & branch might be created by the PO (from QA issue).
  * with POC :
    * POC on **poc_*RUID*-x** subtask & branch from develop (automatically created at adoption).
    * Validate the poc with the PO and the Maintainer.
    * Estimate task difficulty, risk level and time.
  * Add an additional unit test and valid it with the PO.
  * Make technical specifications on **tech-spec_*RUID*-x** subtask & branch from develop .
    * Make technical specifications for his features, refacto or big fix.
    * Identify related general technical specification, get recos from the maintainer.
    * Identify code perimeter :
      * Gitblame to find previous developers on this code section, talk with them about your ideas.
      * Add impacted code perimeter information to the task.
      * Check at daily if others tasks may create any conflicts.
        * Ask maintainer for a tactic to avoid doublon or conflicts.
    * Validate his technical specifications and docs with the maintainer.
    * Explain his tech spec to the dev-team.
  * Creates **feature_*RUID*-x** branch from develop.
    * Develop the feature.
    * Pass the unit tests in a dev-test env automaticly deployed.
  * Ask PO validation for his automated deployed feature.
    * Open new task if the fonctional spec is changed, re-check DoR, re-estimate.
  * Ask the maintainer for code review.
    * Make needed changes.
    * Pass all the tests.
    * Ask the maintainer for code review.
  * (The maintainer check updates and merges potentials conflicts)
  * If **conflict_*RUID*-x_*RUID*-y** subtask have been created by the maintainer:
    * corresponding **conflict_*RUID*-x_*RUID*-y** branch have been created.
    * gitblame identify who will participate to this task.
    * estimate conflict resolution the task.
    * resolve the conflicts.
    * Pass the all the tests.
    * Ask the maintainer for code review.
* If test automation is required :
  * **auto-ut_*RUID*-x** automation unit test subtask is created.
  * **auto-ut_*RUID*-x** branch is created.
  * May ask QA for advices or help.
  * May ask GitOps for help.
  * Develop the tests and organise needed fixtures.
  * Ask the maintainer for code review.
  * Ask QA for automated test review.
  * Ask PO for automated test review.
* If fix **fix_*RUID*-x** subtask is created by the PO :
  * **fix_*RUID*-x** branch is created.
  * May ask PO, QA or MA for advices or help.
  * Fix it
  * Ask PO validation for his automated deployed feature, if not trivial.
  * Ask the maintainer for code review.

### **GOZ** **G**it**O**ps **Z**en:

DevOps using gitlab, advocate and implement best parctices. 

* **Best practices advocates.**
* Help maintainer.
* Help developers for test automation.
* Help QA for test env. and automation.
* Make IPD cosy with the maintainer.
* Help setting cyber security inside the CI/CD pipelines.
* Communicate with DevOps, Infra et security teams.

### **MAZ** - **M**onk **A**gile **Z**en:

Master is a term that is abandonned in branch naming, it is remplaced by main branch.
In a team "Master" or "SM" sado mazo initials may attrack sadists or psycopaths.
The flaccid scrum master is a sample of dramatic miss understanding of agile philosophy.
Monk is better for the ego of an agile consultant.
The Monk Agile, is a team builder and protector, it ensure the cosy spirit needed for best realisations.

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
  * Check IPD is cosy for the dev-team.
  * Check time estimation is done freely.
  * Valorise teams work.
  * Avoid chaos, psychopathy & standford lucifer effects.
* **Tasks management** :
  * Check, maintain tasks status.
  * Check if help or resources are needed.
  * Look for help or resources if asked.
  * Update the tasks boards.
  * Make task boards cosy.
  * Make summary note.