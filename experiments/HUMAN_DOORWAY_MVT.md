# Human Doorway Minimum Viable Test

**Status:** Proposed experiment

## Question

Can a human bring an ordinary, meaningful expression to the Renaissance constellation without knowing which capability or repository should handle it?

## Hypothesis

A useful human doorway does not need to become a new runtime subsystem yet.

The smallest useful proof is a semantic interaction that takes a natural human expression and determines whether it should remain conversational, be clarified, become a Capability Request, or proceed toward an existing capability/instrument.

## Test cases

1. **Conversation**
   - Human says something meaningful but is not asking for capability work.
   - Expected: participate normally; no Capability Request is manufactured.

2. **Clear learning request**
   - Example: "I want to learn how to read a Linux process map."
   - Expected: represent as a Learn Capability Request and enter the existing Learn boundary.

3. **Clear inquiry**
   - Example: "I have two competing explanations for this observation. How could we distinguish them?"
   - Expected: represent as an Understand/investigate Capability Request; if investigation is warranted, create an Attention Choice before Episteme work.

4. **Problem-solving request**
   - Example: "I have this real problem and these constraints. Help me find safe ways to test solutions."
   - Expected: identify Praxis as the appropriate domain capability without silently treating the interpretation as authorization or evidence.

5. **Ambiguous expression**
   - Example: "Something is wrong with this."
   - Expected: clarify rather than invent a capability, target, or action.

6. **Operational request**
   - Example: an existing Organs I/O catalog request.
   - Expected: remain on the established Organs operational path; the Renaissance doorway must not steal or reinterpret operational authority merely because the sentence entered through a human-facing surface.

7. **Unsupported request**
   - Human asks for something outside the established capability vocabulary or available instruments.
   - Expected: say what is not currently supported or ask a useful clarification; fail closed rather than manufacture architecture.

## Pass criteria

The test passes only if:

- natural human expression is preserved;
- conversation is allowed to remain conversation;
- capability interpretation is optional and contextual;
- no capability classification creates authority;
- no Attention Choice is manufactured when no investigation is warranted;
- existing Learn, Episteme, Praxis, and Organs boundaries remain intact;
- ambiguity produces clarification rather than guessing;
- unsupported requests fail honestly;
- the human can understand what the system proposes to do next.

## Important boundary

This experiment does **not** authorize:

- a new Renaissance runtime service;
- a universal intent classifier;
- a new Organs front door;
- autonomous agenda generation;
- universal capability ranking;
- new persistence;
- automatic cross-repository execution.

The experiment is testing the **human interaction boundary**, not implementing a platform.

## Success condition

If the cases can be handled coherently using the existing contracts and instruments, the next question is not "what component should we build?"

It is:

> What actual human interaction is valuable enough to justify making this doorway executable?

If the cases reveal a missing semantic capability, that gap becomes the next architectural question.

If they do not, stop.

