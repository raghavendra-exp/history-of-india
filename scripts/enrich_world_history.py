import json

with open('data/history.json', 'r', encoding='utf-8') as f:
    hdata = json.load(f)

periods = hdata['periods']
period_map = {p['id']: p for p in periods}

# 1. French Revolution
p_fr = period_map.get('french-revolution')
if p_fr:
    p_fr.setdefault('aspects', {})
    p_fr['aspects']['Philosophical & Socio-Fiscal Catalyst (Pratik Nayak World History)'] = [
        "The Three Estates & Tax Inequality: The Ancien Régime was fractured into the First Estate (Clergy, 0.5% population, owning 10% land, exempt from taxes, collecting the Tithe), the Second Estate (Nobility, 1.5% population, exempt from direct taxes, collecting feudal dues), and the Third Estate (Commoners, 98% population - peasantry, urban workers, and bourgeoisie), who bore the entire tax burden (Taille direct land tax, Tithe church tax, Gabelle salt monopoly tax, and Corvée forced labor).",
        "Enlightenment Thinkers: Voltaire exposed ecclesiastical corruption and bigotry; Montesquieu argued for the Separation of Powers ('The Spirit of the Laws'); Jean-Jacques Rousseau conceptualized Popular Sovereignty and the General Will ('The Social Contract'), declaring 'Man is born free, and everywhere he is in chains.'",
        "The Revolutionary Escalation Pipeline: Fiscal bankruptcy from Seven Years' War and funding the American Revolution -> Assembly of Notables deadlock -> Estates-General convened at Versailles (May 1789) -> Third Estate declared the National Assembly -> Tennis Court Oath (20 June 1789) -> Storming of the Bastille (14 July 1789) -> Abolition of Feudalism & Declaration of the Rights of Man and of the Citizen (August 1789).",
        "Radicalization & Terror: Flight to Varennes (1791) discredited the monarchy; French Revolutionary Wars began (Declaration of Pillnitz); National Convention proclaimed the Republic and executed Louis XVI (January 1793); Jacobin Dictatorship under Maximilien Robespierre instituted the Reign of Terror (1793-94) via the Committee of Public Safety and Revolutionary Tribunal, until the Thermidorian Reaction and the eventual rise of Napoleon Bonaparte (1799)."
    ]
    print("Enriched french-revolution")

# 2. American Revolution & Civil War
p_am = period_map.get('american-revolution-and-civil-war')
if p_am:
    p_am.setdefault('aspects', {})
    p_am['aspects']['Causes, Constitutional Synthesis & US-India Comparative Matrix'] = [
        "Colonial Mercantilism & Escalation: Navigation Acts restricted colonial manufacturing; Seven Years' War left Britain in debt, prompting the Sugar Act (1764), Stamp Act (1765 - sparking James Otis's cry 'No taxation without representation!'), Townshend Acts, Boston Massacre (1770), and Boston Tea Party (1773). Lord North's Intolerable/Coercive Acts (1774) galvanized the First Continental Congress.",
        "Declaration of Independence (4 July 1776): Drafted by Thomas Jefferson, grounding revolution in John Locke's social contract and inalienable natural rights (Life, Liberty, and the pursuit of Happiness); military victory secured at Saratoga (1777 - bringing French alliance) and Yorktown (1781) leading to the Treaty of Paris (1783).",
        "American Civil War (1861–1865): Rooted in irreconcilable economic models and the moral crisis of slavery. Agrarian Southern plantation slave economy vs. Northern industrial wage economy; Missouri Compromise (1820), Compromise of 1850, and Dred Scott decision (1857); Abraham Lincoln's election (1860) triggered Southern secession; Emancipation Proclamation (1863) transformed the war into a crusade for human liberty; culminated in Union victory, 13th Amendment abolishing slavery, and preservation of the Union.",
        "Comparative Constitutional Law (USA vs. India Matrix): Federalism: USA is an 'indestructible union of indestructible states', whereas India is an 'indestructible union of destructible states' (Article 3 allows territorial reorganisation without state consent); Executive: US has a rigid Presidential system with strict Separation of Powers, India has a Parliamentary system with executive responsibility to the legislature; Judicial Review: US Constitution follows 'Due Process of Law' (5th & 14th Amendments), whereas India originally instituted 'Procedure Established by Law' (Article 21), later expanding towards substantive due process via the Maneka Gandhi case (1978)."
    ]
    print("Enriched american-revolution-and-civil-war")

# 3. Russian Revolution
p_ru = period_map.get('russian-revolution')
if p_ru:
    p_ru.setdefault('aspects', {})
    p_ru['aspects']['From Tsarist Autocracy to Soviet State (Pratik Nayak World History)'] = [
        "Pre-1917 Structural Crises: Emancipation of Serfs (1861) left peasants laden with redemption dues; rapid industrialization created an impoverished urban proletariat concentrated in giant factories (Putilov works); political autocracy of Tsar Nicholas II; defeat in the Russo-Japanese War (1904-05) triggered Bloody Sunday (January 1905) and the 1905 Revolution, forcing the creation of the State Duma.",
        "The Double Revolution of 1917: February Revolution (March 1917) arose from bread shortages and mutiny in Petrograd, forcing the abdication of Nicholas II and establishing the Dual Power (Provisional Government under Prince Lvov / Alexander Kerensky vs Petrograd Soviet of Workers' and Soldiers' Deputies).",
        "Lenin's April Theses & October Coup: Vladimir Lenin returned from Zurich exile and issued his April Theses: 'All Power to the Soviets', immediate end to the imperialist war, confiscation of landed estates, nationalization of banks. In October (November) 1917, Bolshevik Red Guards led by Leon Trotsky seized key government installations and the Winter Palace with virtually no bloodshed.",
        "Civil War, War Communism & NEP: Bolsheviks signed the punitive Treaty of Brest-Litovsk (March 1918) to exit WWI; fought brutal Russian Civil War (1918-1921, Reds vs Whites and foreign intervention); War Communism (grain requisitioning, nationalization) caused peasant resistance and famine; Lenin pragmatically pivoted to the New Economic Policy (NEP, 1921), reintroducing limited private trade and market mechanisms to resurrect the collapsed economy."
    ]
    print("Enriched russian-revolution")

with open('data/history.json', 'w', encoding='utf-8') as f:
    json.dump(hdata, f, ensure_ascii=False, indent=2)

print("Successfully enriched World History periods in data/history.json!")
