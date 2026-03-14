# PRD Framework

## PRD Structure (10 Sections)

See `../../templates/prd-template.md` for the fillable template.

### Quality Checklist for PRDs
- [ ] Problem is evidence-based (not assumed)
- [ ] Success metrics are measurable (number + direction + timeframe)
- [ ] User is specific (not "users")
- [ ] Scope is clear (in-scope AND out-of-scope defined)
- [ ] Risks are identified with mitigations
- [ ] Technical feasibility confirmed with engineering
- [ ] Launch plan exists
- [ ] No solution smuggling (problem defined before solution)

## User Story Format

### Mike Cohn Format
```
As a [specific persona],
I want to [action/capability],
So that [measurable outcome/benefit].
```

### With Gherkin Acceptance Criteria
```
As a sales manager,
I want to filter leads by engagement score,
So that I can prioritize outreach to the most interested prospects.

Acceptance Criteria:
Given I am on the leads dashboard
When I select "Engagement Score > 70"
Then only leads with score above 70 are displayed
And the count updates to show filtered results
And I can clear the filter to see all leads
```

### Story Splitting Patterns (Richard Lawrence, 8 Patterns)
1. **Workflow steps:** Split by user journey steps
2. **Business rule variations:** Split by different business rules
3. **Major effort:** Extract the hard part as a separate story
4. **Simple/complex:** Do the simple version first
5. **Variations in data:** Split by data types/formats
6. **Data entry methods:** Split by input method (manual, upload, API)
7. **Deferred system qualities:** Performance, security as separate stories
8. **Operations (CRUD):** Split by Create, Read, Update, Delete

### Epic Breakdown Patterns (9 Patterns)
1. User workflow
2. Business rules
3. Happy/sad paths
4. Input methods
5. Data types
6. Platforms
7. Roles/permissions
8. Buy/build components
9. Performance tiers

## Prioritization Frameworks

### RICE Score
**Score = (Reach × Impact × Confidence) / Effort**

| Factor | How to Score |
|--------|-------------|
| Reach | Number of users affected per quarter |
| Impact | 3 (massive), 2 (high), 1 (medium), 0.5 (low), 0.25 (minimal) |
| Confidence | 100% (data-backed), 80% (strong signal), 50% (educated guess) |
| Effort | Person-months required |

### MoSCoW
- **Must Have:** Without this, the release is a failure
- **Should Have:** Important but not critical for this release
- **Could Have:** Nice to have, include if time allows
- **Won't Have:** Explicitly out of scope (this time)

### Kano Model
- **Must-be:** Expected features (absence = dissatisfaction, presence = neutral)
- **One-dimensional:** More = better (linear satisfaction)
- **Attractive:** Unexpected delighters (absence = neutral, presence = delight)
- **Indifferent:** Nobody cares either way
- **Reverse:** Some people like it, some hate it
