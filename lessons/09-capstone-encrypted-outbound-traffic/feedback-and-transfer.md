# Follow-Up Evidence and Transfer Check

Open this file only after completing your initial assessment.

## Part 1: New evidence

Your initial assessment is delivered at 10:15. The software owner and endpoint-response team return the following evidence at 10:42.

These are supplied facts of a fictional written case, not outputs from a deployed lab. The initial packet did not include repository verification history or the effective deployment checks; do not judge the initial assessment using the facts revealed here.

| ID | Source | New observation | Known limitation |
|---|---|---|---|
| F-01 | Vendor security response | AcmeSync states that version 4.8.2 does not use `telemetry.acmesync.example` and that the domain is not vendor controlled. | The statement does not yet explain how the unauthorized package entered the environment. |
| F-02 | Vendor release manifest | The approved `AcmeSyncUpdater.exe` hash differs from the hash shared by all 37 online updated systems. | Hash difference establishes a binary mismatch, not the binary's complete behavior. |
| F-03 | Deployment repository audit and job configuration | The approved artifact was checked against the release manifest at 08:30. A mismatched package replaced it at the same repository path at 08:41 using a valid automation credential. The 09:00 job read that mutable path without comparing the deployed bytes with the approved manifest again. | This establishes a gap between staging verification and deployment, not whether the credential or automation host was compromised. |
| F-04 | Endpoint-response comparison | The deployed package contains a validly signed updater binary different from the approved release plus an unsigned module absent from the known-good package. The updater loads that module and creates persistence before initiating the recurring connection. | A valid executable signature does not approve the package/version or all dependencies. The team has not completed malware analysis or determined the full impact. |
| F-05 | Network scope check | All 37 online updated systems show the same destination and connection pattern; systems that did not receive 4.8.2 do not. | Offline systems and activity before available retention remain unassessed. |

## Revision task

Revise your work product. Keep the revision concise, but make the change visible:

- State your revised assessment, confidence, and recommended action.
- Identify which new evidence changed the leading explanation and why.
- Explain what the peer similarity means now compared with what it meant initially.
- Preserve any uncertainty that still matters.
- Provide a usable handoff for the software owner, endpoint-response team, and whoever owns the deployment credential or automation host.
- Compare your initial and revised models. A revision is not a failure when it responds appropriately to evidence that was previously unavailable.

For the handoff, keep ownership explicit: the deployment administrator pauses the job and protects the repository; the identity team handles the automation credential; endpoint responders preserve and investigate host evidence; the software owner coordinates workflow impact and vendor confirmation. Network/security engineering implements approved scoped controls. The operational decision owner coordinates authorization. The network analyst supplies the integrated assessment and scoped evidence, not every specialist action.

## Part 2: Transfer to a different situation

Later, you review an unrelated office incident. Intermittent DNS failures began shortly after 08:00. An initial analyst attributed the failures to periodic, encoded-looking queries to `inventory.agent.example` and recommended blocking the domain.

Peer feedback notes that the claim relies heavily on the appearance of the query and does not test history, path behavior, or comparison segments. You obtain this evidence:

| ID | Observation |
|---|---|
| T-01 | The same inventory queries appear in 21 prior days without service failure. |
| T-02 | Asset records identify the queries as an authorized inventory agent's behavior. |
| T-03 | A firewall policy affecting the office path changed at 07:55. |
| T-04 | Resolver-side capture shows successful upstream responses around 1,680 bytes; affected clients show queries and retransmissions but no complete UDP response. |
| T-05 | The policy drops non-initial IP fragments and does not permit DNS TCP fallback for the office segment. |
| T-06 | A comparison office without the policy change resolves the same domains successfully while producing the same inventory queries. |
| T-07 | A temporary rollback restores resolution immediately; inventory queries continue unchanged. |

Produce a short transfer response:

1. What causal explanation now best fits the evidence?
2. Which observations discriminate it from the initial tunneling explanation?
3. What proportionate correction or next action follows?
4. What general reasoning practice transferred from the encrypted-traffic case even though the technology and outcome changed?

When finished, open the [review guide](review-guide.md).
