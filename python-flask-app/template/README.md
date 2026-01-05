# ${{values.name}}

## ${{values.uid}}

- deployment environements : ${{values.environements}}
- owner: ${{values.owner}}

## Application documentation

[DOC](docs/index.md)

## **ZAT** - **Z**en  **A**gile **T**eam

### **POZ** - **P**roduct **O**wner **Z**en:

Final Product Responsable - decide how the product must work for final users.

* **Functional Specifications Redaction** :
  * Responsable for general functional specifications.
  * Responsable for detailed functional specifications.
  * Take in account technical specification constraints and requirements.
* **Manage Fonctional Epics and Milestones** (taking in account technicals necessities).
* **Manage Requirements** :
  * Organise functionnal requirements :
    * UID - **req-uid**
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
  * Create **func-spec_*req-uid*-x** functional specification tasks.
    * Feature description :
      * Related general specification version, chapter and section.
      * Requirement uid.
      * context : pages, user roles, action, entities, status-step-event.
      * what action ?
      * what result ?
      * how to test it is working ?
      * fixtures and an example.
    * Ensure the developers got a good understanding of the new features
    * Ensure there is no doublons
    * Ensure features are linked with an exigence.
* **Feature Fonctional Unit Tests & Validation**.
* Create **fix_*req-uid*-x** **fix** or **hotfix** tasks.
  * describe the bug or refining for **func-spec_*req-uid*-x**.
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

### **QAZ** - **Q**uality **A**ssement **Z**en :

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

* **Best technical pratices advocate**.
* **Lead the global technical specifications**.
  * Validate features technical specifications.
  * Anticipate and manage code conflicts or doublons.
* **Manage Technical Epics and Milestones.**
* **Organise technical requirements (according to functional needs)** :
  * UID - **req-uid**
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
        * **conflict_*req-uid*-x** subtask and branch is created
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
  
### **ZED** - **Z**en **E**xpert **D**evelopers:

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
* Adopt a feature alone or with a binome.
  * with POC :
    * Creates **poc_*req-uid*-x** subtask & branch from develop.
    * Validate the poc with the PO and the Maintainer.
    * Estimate task difficulty, risk level and time.
  * Add an additional unit test and valid it with the PO.
  * Creates **tech-spec_*req-uid*-x** subtask & branch from develop.
    * Make technical specifications for his features, refacto or big fix.
    * Identify related general technical specification, get recos from the maintainer.
    * Identify code perimeter :
      * Gitblame to find previous developers on this code section, talk with them about your ideas.
      * Add impacted code perimeter information to the task.
      * Check at daily if others tasks may create any conflicts.
        * Ask maintainer for a tactic to avoid doublon or conflicts.
    * Validate his technical specifications and docs with the maintainer.
    * Explain his tech spec to the dev-team.
  * Creates **feature_*req-uid*-x** branch from develop.
    * Develop the feature.
    * Pass the unit tests in a dev-test env automaticly deployed.
  * Ask PO validation for his automated deployed feature.
    * Open new task if the fonctional spec is changed, re-check DoR, re-estimate.
  * Ask the maintainer for code review.
    * Make needed changes.
    * Pass all the tests.
    * Ask the maintainer for code review.
  * (The maintainer check updates and merges potentials conflicts)
  * If **conflict_*req-uid*-x** subtask is created:
    * **conflict_*req-uid*-x** branch is created.
    * gitblame identify who will participate to this task.
    * estimate conflict resolution the task.
    * resolve the conflicts.
    * Pass the all the tests.
    * Ask the maintainer for code review.
* If test automation is required :
  * **auto-ut_*req-uid*-x** automation unit test task is created.
  * **auto-ut_*req-uid*-x** branch is created.
  * May ask QA for advices or help.
  * May ask GitOps for help.
  * Develop the tests and organise needed fixtures.
  * Ask the maintainer for code review.
  * Ask QA for automated test review.
  * Ask PO for automated test review.

### GitOps:

* **Best practices advocates.**
* Help maintainer.
* Help developers for test automation.
* Help QA for test env. and automation.
* Make IPD cosy with the maintainer.

### **ZAM** - **Z**en **A**gile **M**onk:

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