# WorkearlyFinalAssignment

1. Αντέγραψα τον κώδικα που βρίσκεται στο αναρτημένο "finance_liquor_sales.sql", τον επικόλλησα στο Workbench και έκανα εξαγωγή σε αρχείο .csv τον εξής κώδικα:
select * from finance_liquor_sales as f
where f.date >= '2016-01-01' and f.date <= '2019-12-31' 
order by f.date asc;

2. Στη συνέχεια χρησιμοποίησα το αρχείο .csv για να δημιουργήσω ένα γράφημα Matplotlib στο PyCharm. Ο κώδικας του γραφήματος βρίσκεται αναρτημένος εδώ.
Αντιμετώπισα δυσκολία στο γκρουπάρισμα, καθώς μετά το γκουπάρισμα δεν δεχόταν τις αξίες του άξονα y, μου έβγαζε error. Με τη βοήθειά σας χρησιμοποίησα τελικά τον κώδικα zc = df.groupby(['zip_code', 'item_description']).sum().sort_values("bottles_sold", ascending=False)
item_description = zc.index.get_level_values('item_description') που όμως ακόμα δεν καταλαβαίνω τη λογική του, παρόλο που σας ρώτησα στο Skype.

3. Στη συνέχεια χρησιμοποίησα πάλι το αρχείο csv "finance_liquor_sales.sql" στο Tableau, όπου έκανα τις αναλύσεις με οδηγό τις εικόνες που έβλεπα στην εκφώνηση της εργασίας. Εκεί δεν συνάντησα ιδιαίτερο πρόβλημα, μόνο συνειδητοποίησα ότι ήμουν "σκουριασμένος", επειδή δεν είχα ασχοληθεί με Tableau για μήνες.
