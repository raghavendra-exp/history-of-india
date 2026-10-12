import json

with open('data/mains-questions.json', 'r', encoding='utf-8') as f:
    mains = json.load(f)

more_mains = [
    {
        "id": "mains-pn-008",
        "question": "The Royal Indian Navy (RIN) Mutiny of February 1946 shattered the final military pillar of the British Raj. Evaluate its significance in the transfer of power.",
        "marks": 10,
        "wordLimit": 150,
        "bookRef": "Pratik Nayak HFS12P1; B.L. Grover; Bipan Chandra, Ch. 36",
        "framework": {
            "intro": "On 18 February 1946, 1,100 naval ratings on HMIS Talwar in Bombay went on strike against racial discrimination, bad food, and the ongoing INA trials. Within 48 hours, the mutiny spread across 78 ships, 20 shore establishments, and 20,000 ratings in Bombay, Karachi, and Calcutta, signaling that the armed forces could no longer be relied upon to sustain colonial rule.",
            "body": [
                {
                    "heading": "Military & Popular Impact",
                    "points": [
                        "Communal & Cross-Service Solidarity: Ratings hoisted Congress tricolors, Muslim League crescents, and Red flags tied together on ship masts; strikes broke out among Royal Indian Air Force (RIAF) units and army signal corps.",
                        "Mass Working-Class Support: In Bombay, over 300,000 workers went on a general strike in solidarity; hundreds were shot by British troops on the barricades before Sardar Patel and Jinnah persuaded the naval strike committee to surrender on 23 February.",
                        "Demolition of Imperial Coercion: As Prime Minister Clement Attlee later acknowledged, when the Indian army, navy, and air force ceased to be obedient instruments of British repression, colonial rule became physically untenable."
                    ]
                },
                {
                    "heading": "Catalyst to Transfer of Power",
                    "points": [
                        "Dispatch of Cabinet Mission: The mutiny broke out on 18 February; on 19 February, Prime Minister Attlee announced the immediate dispatch of the Cabinet Mission to negotiate the transfer of power.",
                        "Advancing the Independence Timeline: Proved to the British Chiefs of Staff that holding India required massive British troop deployments that war-weary Britain could not afford."
                    ]
                }
            ],
            "conclusion": "The RIN Mutiny was the final nail in the coffin of British imperial rule in India. It demonstrated that the sword of the Raj had broken in its own hands.",
            "diagramMapIdea": "Impact Chain: HMIS Talwar Strike -> Multi-Fleet Spread -> Popular Working-Class Strikes -> Military Unreliability realized in Whitehall -> Cabinet Mission announcement (19 Feb 1946) -> Independence."
        }
    },
    {
        "id": "mains-pn-009",
        "question": "Examine the role of parallel governments during the Quit India Movement of 1942, with special reference to Ballia, Tamluk, and Satara.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak HFS11P1; Bipan Chandra, Ch. 35; Spectrum Modern India",
        "framework": {
            "intro": "The Quit India Movement of August 1942 reached its revolutionary peak in the establishment of 'Parallel Governments' (Prati Sarkar / Jatiya Sarkar) in rural strongholds where colonial authority was completely overthrown and popular sovereign institutions functioned for weeks and months.",
            "body": [
                {
                    "heading": "Ballia (Uttar Pradesh) — The Spontaneous Surge",
                    "points": [
                        "Chittu Pandey's Leadership: In August 1942, the populace overthrew British administration in Ballia, forced the District Magistrate to hand over authority, released all Congress prisoners, and proclaimed independent rule under Chittu Pandey ('Sher-e-Ballia') for a week before British troops reoccupied the town."
                    ]
                },
                {
                    "heading": "Tamluk (Midnapore, Bengal) — Jatiya Sarkar & Cyclone Relief",
                    "points": [
                        "Institutional Resilience: The Tamluk Jatiya Sarkar functioned from December 1942 to September 1944.",
                        "Vidyut Vahini & Martyrdom: Maintained an organized volunteer defense corps (Vidyut Vahini); 73-year-old Matangini Hazra was shot dead while holding the national flag high; ran people's arbitration courts and distributed grain during the catastrophic Bengal Famine of 1943."
                    ]
                },
                {
                    "heading": "Satara (Maharashtra) — Prati Sarkar & People's Courts",
                    "points": [
                        "Longest Lasting Parallel Government: Led by Nana Patil, Y.B. Chavan, and Kisan Veer, operating from mid-1943 to 1945.",
                        "Nyayadan Mandals: Set up village people's courts (Nyayadan Mandals) to resolve civil and criminal disputes without colonial police; penalized rapists and dacoits; organized grain banks and market price controls, gaining deep peasant loyalty."
                    ]
                }
            ],
            "conclusion": "These parallel governments proved that ordinary Indian peasants were not merely capable of resisting foreign rule, but of organizing just, democratic, and welfare-oriented self-governance in the face of brutal state violence.",
            "diagramMapIdea": "Comparative Regional Matrix: Ballia (Chittu Pandey - Spontaneous week-long seizure), Tamluk (Jatiya Sarkar - 2-year institutional governance, Vidyut Vahini, famine relief), Satara (Prati Sarkar - Nyayadan Mandals, Nana Patil, grain distribution)."
        }
    },
    {
        "id": "mains-wh-001",
        "question": "The French Revolution dismantled the feudal structures of the Ancien Régime but unleashed unprecedented political terror. Discuss the transition from the Declaration of the Rights of Man to the Jacobin Dictatorship.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak WH_Fr; Norman Lowe, Ch. 1; NCERT Class 9 World History",
        "framework": {
            "intro": "The French Revolution (1789) erupted with the universal promise of 'Liberty, Equality, Fraternity' encapsulated in the 1789 Declaration of the Rights of Man and of the Citizen. Yet within four years, revolutionary idealism descended into the draconian Jacobin Reign of Terror (1793–1794) under Maximilien Robespierre.",
            "body": [
                {
                    "heading": "The Idealistic Dawn: Abolition of Feudal Privileges",
                    "points": [
                        "August Decrees (1789): National Assembly dismantled feudalism, abolished tithes, and erased aristocratic tax exemptions.",
                        "Declaration of the Rights of Man (26 August 1789): Proclaimed inalienable rights to liberty, property, security, and resistance to oppression; declared that sovereignty resides essentially in the Nation."
                    ]
                },
                {
                    "heading": "Factors Fueling Radicalization and the Descent into Terror",
                    "points": [
                        "Foreign War & Counter-Revolution: The Declaration of Pillnitz and Austrian/Prussian invasion threatened the Revolution; King Louis XVI's treasonous Flight to Varennes destroyed monarchical credibility.",
                        "Internal Insurrection: Peasant royalist revolt in the Vendée and federalist uprisings in Lyon and Marseille threatened state collapse.",
                        "Economic Scarcity: Skyrocketing bread prices and depreciation of the Assignat currency radicalized the urban Sans-Culottes."
                    ]
                },
                {
                    "heading": "The Jacobin Dictatorship & Committee of Public Safety",
                    "points": [
                        "Maximilien Robespierre's 'Virtue and Terror': Instituted the Committee of Public Safety; passed the Law of Suspects (September 1793); over 40,000 people guillotined across France.",
                        "De-Christianization & Totalitarian Control: Established the Cult of the Supreme Being, revolutionary calendar, and fixed maximum grain prices (Law of the Maximum), alienating the peasantry.",
                        "Thermidorian Reaction: The Terror devoured its own children (Danton, Desmoulins), culminating in Robespierre's overthrow on 9 Thermidor (July 1794)."
                    ]
                }
            ],
            "conclusion": "The French Revolution demonstrated the tragic peril of pursuing abstract virtue through tyrannical coercion. While the Terror perished with Robespierre, the foundational principles of 1789 survived to become the bedrock of modern global democracy.",
            "diagramMapIdea": "Timeline Escalation Pipeline: Estates-General (May 1789) -> Bastille (July 1789) -> Rights of Man (Aug 1789) -> War & Flight to Varennes (1791-92) -> Execution of King (Jan 1793) -> Reign of Terror (1793-94) -> Thermidorian Reaction."
        }
    },
    {
        "id": "mains-wh-002",
        "question": "Compare the constitutional provisions regarding executive governance and judicial review in the United States and India.",
        "marks": 15,
        "wordLimit": 250,
        "bookRef": "Pratik Nayak CmC_P1&2; Norman Lowe; Indian Polity by M. Laxmikanth",
        "framework": {
            "intro": "The United States and India represent the world's oldest and largest constitutional democracies. While India drew heavily from the American constitutional experience, its framers adapted key institutions to suit India's socio-cultural pluralism and historical imperatives.",
            "body": [
                {
                    "heading": "Executive Governance: Presidential vs. Parliamentary System",
                    "points": [
                        "United States (Presidential System): Strict Separation of Powers under Montesquieu's model; President is both Head of State and Head of Government, directly elected via Electoral College for a fixed 4-year term, and not accountable to Congress.",
                        "India (Parliamentary System): Fused executive and legislative branches; President is nominal/titular Head of State acting on the binding aid and advice of the Council of Ministers (Article 74) headed by the Prime Minister (real executive), who is collectively responsible to the Lok Sabha (Article 75)."
                    ]
                },
                {
                    "heading": "Judicial Review: Due Process vs. Procedure Established by Law",
                    "points": [
                        "American Model (Due Process of Law): Established in Marbury v. Madison (1803) and 5th/14th Amendments. Courts evaluate not only whether the legislature had procedural competence to pass a law, but whether the substantive content of the law is just, fair, and reasonable.",
                        "Indian Model (Procedure Established by Law -> Substantive Due Process): Originally drafted under Article 21 from the Japanese/British model ('Procedure Established by Law', A.K. Gopalan case 1950). However, through the landmark Maneka Gandhi case (1978), the Supreme Court integrated substantive Due Process, establishing that procedure must be 'right, just, and fair'."
                    ]
                },
                {
                    "heading": "Federal Structure Comparison",
                    "points": [
                        "US: An 'indestructible union of indestructible states'; states have their own constitutions, dual citizenship, and state boundaries cannot be altered without consent.",
                        "India: An 'indestructible union of destructible states' (Article 3 gives Parliament sole power to alter boundaries and create new states without state consent); single citizenship and unified integrated judiciary."
                    ]
                }
            ],
            "conclusion": "The American Constitution prioritized individual liberty and strict separation of powers for a pioneer society, while the Indian Constitution prioritized responsible parliamentary governance and social transformation for a newly emerging republic.",
            "diagramMapIdea": "Comparative 3-Column Table: Dimension (Executive, Judicial Review, Federal Nature), USA Model, and Indian Model."
        }
    }
]

existing_ids = set(m['id'] for m in mains)
added_count = 0
for nm in more_mains:
    if nm['id'] not in existing_ids:
        mains.append(nm)
        existing_ids.add(nm['id'])
        added_count += 1

with open('data/mains-questions.json', 'w', encoding='utf-8') as f:
    json.dump(mains, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} more Mains questions. Total now: {len(mains)}")
