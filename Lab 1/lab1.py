def rule(score, documents_complete, semesters_completed, days_since_open):
    if not documents_complete:
        return "Hold", "Documents incomplete"
    if score < 70:
        return "Hold", "Score less than 70"
    if semesters_completed < 2:
        return "Hold", "Fewer than two completed semesters"
    if days_since_open > 10:
        return "Hold", "Submission after day 10"
    return "Review", "All stated conditions passed"

def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"

cases = [
    ("pass", 85, True, 3, 4, .83, "Review"),
    ("semesters_fail", 86, True, 1, 3, .88, "Hold"),
    ("timing_fail", 90, True, 4, 14, .91, "Hold"),
    ("all_boundaries", 70, True, 2, 10, .70, "Review"),
]
print("CASE | INPUT(score,documents,semesters,day,prob) | EXPECTED | ACTUAL | REASON | THRESHOLD | DISAGREE")
for name,score,complete,semester,day,p,expected in cases:
    actual,reason=rule(score,complete,semester,day)
    other=threshold(p)
    print(name,(score,complete,semester,day,p),expected,actual,reason,other,actual!=other,sep=" | ")
    assert actual==expected
print("ADDITIONAL EDGE CHECKS")
for item in [(94,False,4,3,.93),(69,True,3,2,.69),(70,True,2,11,.70)]:
    print(item,rule(*item[:4]),threshold(item[4]))
