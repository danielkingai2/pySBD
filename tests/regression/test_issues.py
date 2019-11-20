# -*- coding: utf-8 -*-
import pytest
import pysbd
from pysbd.utils import TextSpan

TEST_ISSUE_DATA = [
    ('#27', "This new form of generalized PDF in (9) is generic and suitable for all the fading models presented in Table I withbranches MRC reception. In section III, (9) will be used in the derivations of the unified ABER and ACC expression.",
        ["This new form of generalized PDF in (9) is generic and suitable for all the fading models presented in Table I withbranches MRC reception.",
         "In section III, (9) will be used in the derivations of the unified ABER and ACC expression."]),
    ('#29', "Random walk models (Skellam, 1951;Turchin, 1998) received a lot of attention and were then extended to several more mathematically and statistically sophisticated approaches to interpret movement data such as State-Space Models (SSM) (Jonsen et al., 2003(Jonsen et al., , 2005 and Brownian Bridge Movement Model (BBMM) (Horne et al., 2007). Nevertheless, these models require heavy computational resources (Patterson et al., 2008) and unrealistic structural a priori hypotheses about movement, such as homogeneous movement behavior. A fundamental property of animal movements is behavioral heterogeneity (Gurarie et al., 2009) and these models poorly performed in highlighting behavioral changes in animal movements through space and time (Kranstauber et al., 2012).",
        ["Random walk models (Skellam, 1951;Turchin, 1998) received a lot of attention and were then extended to several more mathematically and statistically sophisticated approaches to interpret movement data such as State-Space Models (SSM) (Jonsen et al., 2003(Jonsen et al., , 2005 and Brownian Bridge Movement Model (BBMM) (Horne et al., 2007).",
         "Nevertheless, these models require heavy computational resources (Patterson et al., 2008) and unrealistic structural a priori hypotheses about movement, such as homogeneous movement behavior.",
         "A fundamental property of animal movements is behavioral heterogeneity (Gurarie et al., 2009) and these models poorly performed in highlighting behavioral changes in animal movements through space and time (Kranstauber et al., 2012)."]),
    ('#30', "Thus, we first compute EMC 3 's response time-i.e., the duration from the initial of a call (from/to a participant in the target region) to the time when the decision of task assignment is made; and then, based on the computed response time, we estimate EMC 3 maximum throughput [28]-i.e., the maximum number of mobile users allowed in the MCS system. EMC 3 algorithm is implemented with the Java SE platform and is running on a Java HotSpot(TM) 64-Bit Server VM; and the implementation details are given in Appendix, available in the online supplemental material.",
        ["Thus, we first compute EMC 3 's response time-i.e., the duration from the initial of a call (from/to a participant in the target region) to the time when the decision of task assignment is made; and then, based on the computed response time, we estimate EMC 3 maximum throughput [28]-i.e., the maximum number of mobile users allowed in the MCS system.",
         "EMC 3 algorithm is implemented with the Java SE platform and is running on a Java HotSpot(TM) 64-Bit Server VM; and the implementation details are given in Appendix, available in the online supplemental material."
        ]),
    ('#31', r"Proof. First let v ∈ V be incident to at least three leaves and suppose there is a minimum power dominating set S of G that does not contain v. If S excludes two or more of the leaves of G incident to v, then those leaves cannot be dominated or forced at any step. Thus, S excludes at most one leaf incident to v, which means S contains at least two leaves ℓ 1 and ℓ 2 incident to v. Then, (S\{ℓ 1 , ℓ 2 }) ∪ {v} is a smaller power dominating set than S, which is a contradiction. Now consider the case in which v ∈ V is incident to exactly two leaves, ℓ 1 and ℓ 2 , and suppose there is a minimum power dominating set S of G such that {v, ℓ 1 , ℓ 2 } ∩ S = ∅. Then neither ℓ 1 nor ℓ 2 can be dominated or forced at any step, contradicting the assumption that S is a power dominating set. If S is a power dominating set that contains ℓ 1 or ℓ 2 , say ℓ 1 , then (S\{ℓ 1 }) ∪ {v} is also a power dominating set and has the same cardinality. Applying this to every vertex incident to exactly two leaves produces the minimum power dominating set required by (3). Definition 3.4. Given a graph G = (V, E) and a set X ⊆ V , define ℓ r (G, X) as the graph obtained by attaching r leaves to each vertex in X. If X = {v 1 , . . . , v k }, we denote the r leaves attached to vertex v i as ℓ",
        ['Proof.', 'First let v ∈ V be incident to at least three leaves and suppose there is a minimum power dominating set S of G that does not contain v. If S excludes two or more of the leaves of G incident to v, then those leaves cannot be dominated or forced at any step.', 'Thus, S excludes at most one leaf incident to v, which means S contains at least two leaves ℓ 1 and ℓ 2 incident to v. Then, (S\\{ℓ 1 , ℓ 2 }) ∪ {v} is a smaller power dominating set than S, which is a contradiction.', 'Now consider the case in which v ∈ V is incident to exactly two leaves, ℓ 1 and ℓ 2 , and suppose there is a minimum power dominating set S of G such that {v, ℓ 1 , ℓ 2 } ∩ S = ∅.', 'Then neither ℓ 1 nor ℓ 2 can be dominated or forced at any step, contradicting the assumption that S is a power dominating set.', 'If S is a power dominating set that contains ℓ 1 or ℓ 2 , say ℓ 1 , then (S\\{ℓ 1 }) ∪ {v} is also a power dominating set and has the same cardinality.', 'Applying this to every vertex incident to exactly two leaves produces the minimum power dominating set required by (3).', 'Definition 3.4.', 'Given a graph G = (V, E) and a set X ⊆ V , define ℓ r (G, X) as the graph obtained by attaching r leaves to each vertex in X. If X = {v 1 , . . . , v k }, we denote the r leaves attached to vertex v i as ℓ']),
    ('#34', '.', ['.']),
    ('#34', '..', ['..']),
    ('#34', '. . .', ['. . .']),
    ('#34', '! ! !', ['! ! !']),
    ('#36', '??', ['??']),
    ('#37', "As an example of a different special-purpose mechanism, we have introduced a methodology for letting donors make their donations to charities conditional on donations by other donors (who, in turn, can make their donations conditional) [70]. We have used this mechanism to collect money for Indian Ocean Tsunami and Hurricane Katrina victims. We have also introduced a more general framework for negotiation when one agent's actions have a direct effect (externality) on the other agents' utilities [69]. Both the charities and externalities methodologies require the solution of NP-hard optimization problems in general, but there are some natural tractable cases as well as effective MIP formulations. Recently, Ghosh and Mahdian [86] at Yahoo! Research extended our charities work, and based on this a web-based system for charitable donations was built at Yahoo!",
     ['As an example of a different special-purpose mechanism, we have introduced a methodology for letting donors make their donations to charities conditional on donations by other donors (who, in turn, can make their donations conditional) [70].', 'We have used this mechanism to collect money for Indian Ocean Tsunami and Hurricane Katrina victims.', "We have also introduced a more general framework for negotiation when one agent's actions have a direct effect (externality) on the other agents' utilities [69].", 'Both the charities and externalities methodologies require the solution of NP-hard optimization problems in general, but there are some natural tractable cases as well as effective MIP formulations.', 'Recently, Ghosh and Mahdian [86] at Yahoo! Research extended our charities work, and based on this a web-based system for charitable donations was built at Yahoo!']),
    ('#39', "T stands for the vector transposition. As shown in Fig. ??",
     ["T stands for the vector transposition.", "As shown in Fig. ??"]),
    ('#39', 'Fig. ??', ['Fig. ??'])
]

@pytest.mark.parametrize('issue_no,text,expected_sents', TEST_ISSUE_DATA)
def test_issue(issue_no, text, expected_sents):
    """pySBD issues tests from https://github.com/nipunsadvilkar/pySBD/issues/"""
    seg = pysbd.Segmenter(language="en", clean=False)
    segments = seg.segment(text)
    assert segments == expected_sents
    # clubbing sentences and matching with original text
    assert text == " ".join(segments)

@pytest.mark.parametrize('issue_no,text,expected',
                         [
                            ('#49', 'This list has some numbers like 1) The first item. 2) The second item.',
                              [
                                  TextSpan(sent='This list has some numbers like', start=0, end=31),
                                  TextSpan(sent='1) The first item.', start=32, end=50),
                                  TextSpan(sent='2) The second item.', start=51, end=70)
                              ]
                             ),
                             ('#49', 'a. The first item b. The second item c. The third list item',
                              [
                                 TextSpan(sent='a. The first item', start=0, end=17),
                                 TextSpan(sent='b. The second item', start=18, end=36),
                                 TextSpan(sent='c. The third list item', start=37, end=59)
                               ]
                              )
                         ])
def test_carriage_return_cases(issue_no,text, expected):
    """Test carriage return sentences with character offsets"""
    seg = pysbd.Segmenter(language="en", clean=False, char_span=True)
    segments = seg.segment(text)
    assert segments == expected
