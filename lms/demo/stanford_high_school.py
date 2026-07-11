"""Deterministic, synthetic demo data for Stanford High School.

The people in this module are fictional. Email addresses use the reserved
``.example`` domain so the seed cannot accidentally contact real people.
"""

from __future__ import annotations

import re
from collections import Counter

import frappe
from frappe import _

SCHOOL_NAME = "Stanford High School"
ACADEMIC_YEAR = "2026-27"
START_DATE = "2026-08-24"
END_DATE = "2027-06-11"
TIMEZONE = "America/Los_Angeles"
SYNTHETIC_DATA_NOTICE = (
	"All names and records in this dataset are fictional and intended only for testing and demonstrations."
)

PERIODS = {
	1: ("08:00:00", "08:50:00"),
	2: ("09:00:00", "09:50:00"),
	3: ("10:00:00", "10:50:00"),
	4: ("11:00:00", "11:50:00"),
	5: ("12:30:00", "13:20:00"),
	6: ("13:30:00", "14:20:00"),
	7: ("14:30:00", "15:20:00"),
}

TEACHERS = (
	{"key": "margaret.ellis", "first_name": "Margaret", "last_name": "Ellis", "department": "English"},
	{"key": "jonathan.reed", "first_name": "Jonathan", "last_name": "Reed", "department": "English"},
	{"key": "aisha.rahman", "first_name": "Aisha", "last_name": "Rahman", "department": "English"},
	{"key": "claire.robinson", "first_name": "Claire", "last_name": "Robinson", "department": "English"},
	{"key": "daniel.brooks", "first_name": "Daniel", "last_name": "Brooks", "department": "Mathematics"},
	{"key": "priya.raman", "first_name": "Priya", "last_name": "Raman", "department": "Mathematics"},
	{"key": "lucas.bennett", "first_name": "Lucas", "last_name": "Bennett", "department": "Mathematics"},
	{"key": "robert.hayes", "first_name": "Robert", "last_name": "Hayes", "department": "Mathematics"},
	{"key": "elena.martinez", "first_name": "Elena", "last_name": "Martinez", "department": "Science"},
	{"key": "samuel.price", "first_name": "Samuel", "last_name": "Price", "department": "Science"},
	{"key": "mei-lin.chen", "first_name": "Mei-Lin", "last_name": "Chen", "department": "Science"},
	{"key": "natalie.foster", "first_name": "Natalie", "last_name": "Foster", "department": "Science"},
	{"key": "marcus.green", "first_name": "Marcus", "last_name": "Green", "department": "Science"},
	{"key": "thomas.nguyen", "first_name": "Thomas", "last_name": "Nguyen", "department": "Social Studies"},
	{"key": "grace.kim", "first_name": "Grace", "last_name": "Kim", "department": "Social Studies"},
	{"key": "david.cooper", "first_name": "David", "last_name": "Cooper", "department": "Social Studies"},
	{"key": "michael.turner", "first_name": "Michael", "last_name": "Turner", "department": "Social Studies"},
	{"key": "victor.chen", "first_name": "Victor", "last_name": "Chen", "department": "Computer Science"},
	{"key": "maya.singh", "first_name": "Maya", "last_name": "Singh", "department": "Computer Science"},
	{
		"key": "christopher.hall",
		"first_name": "Christopher",
		"last_name": "Hall",
		"department": "Computer Science",
	},
	{"key": "noah.williams", "first_name": "Noah", "last_name": "Williams", "department": "Computer Science"},
	{"key": "sofia.alvarez", "first_name": "Sofia", "last_name": "Alvarez", "department": "World Languages"},
	{
		"key": "javier.morales",
		"first_name": "Javier",
		"last_name": "Morales",
		"department": "World Languages",
	},
	{"key": "isabel.rivera", "first_name": "Isabel", "last_name": "Rivera", "department": "World Languages"},
	{"key": "emily.carter", "first_name": "Emily", "last_name": "Carter", "department": "Arts"},
	{"key": "lila.thompson", "first_name": "Lila", "last_name": "Thompson", "department": "Arts"},
	{"key": "rachel.stein", "first_name": "Rachel", "last_name": "Stein", "department": "Arts"},
	{"key": "hannah.patel", "first_name": "Hannah", "last_name": "Patel", "department": "Learning Support"},
	{
		"key": "benjamin.collins",
		"first_name": "Benjamin",
		"last_name": "Collins",
		"department": "Learning Support",
	},
)

CLASS_SPECS = (
	{
		"code": "ENG-09-01",
		"title": "English Literature 9",
		"department": "English",
		"grades": (9,),
		"period": 1,
		"roster_size": 22,
		"teachers": ("margaret.ellis", "jonathan.reed", "hannah.patel"),
		"focus": "close reading, analytical writing, and discussion of classic and contemporary literature",
	},
	{
		"code": "ENG-10-02",
		"title": "World Literature 10",
		"department": "English",
		"grades": (10,),
		"period": 2,
		"roster_size": 23,
		"teachers": ("jonathan.reed", "aisha.rahman", "hannah.patel"),
		"focus": "global literary traditions, comparative analysis, and evidence-based composition",
	},
	{
		"code": "ENG-11-03",
		"title": "American Literature 11",
		"department": "English",
		"grades": (11,),
		"period": 3,
		"roster_size": 21,
		"teachers": ("margaret.ellis", "claire.robinson", "hannah.patel"),
		"focus": "American voices, rhetorical context, research, and seminar-style discussion",
	},
	{
		"code": "ENG-AP-04",
		"title": "AP English Language and Composition",
		"department": "English",
		"grades": (11, 12),
		"period": 4,
		"roster_size": 20,
		"teachers": ("aisha.rahman", "claire.robinson", "jonathan.reed"),
		"focus": "advanced rhetoric, argumentation, synthesis, and timed analytical writing",
	},
	{
		"code": "MAT-A1-05",
		"title": "Algebra I",
		"department": "Mathematics",
		"grades": (9,),
		"period": 5,
		"roster_size": 25,
		"teachers": ("daniel.brooks", "priya.raman", "benjamin.collins"),
		"focus": "linear relationships, functions, systems of equations, and mathematical modeling",
	},
	{
		"code": "MAT-GE-06",
		"title": "Geometry",
		"department": "Mathematics",
		"grades": (9, 10),
		"period": 6,
		"roster_size": 24,
		"teachers": ("lucas.bennett", "robert.hayes", "benjamin.collins"),
		"focus": "proof, spatial reasoning, transformations, measurement, and applied geometry",
	},
	{
		"code": "MAT-A2-07",
		"title": "Algebra II",
		"department": "Mathematics",
		"grades": (10, 11),
		"period": 7,
		"roster_size": 22,
		"teachers": ("priya.raman", "lucas.bennett", "benjamin.collins"),
		"focus": "polynomial, exponential, logarithmic, and rational functions with data applications",
	},
	{
		"code": "MAT-PC-01",
		"title": "Precalculus",
		"department": "Mathematics",
		"grades": (11, 12),
		"period": 1,
		"roster_size": 20,
		"teachers": ("daniel.brooks", "robert.hayes", "priya.raman"),
		"focus": "advanced functions, trigonometry, analytic geometry, and preparation for calculus",
	},
	{
		"code": "SCI-BI-02",
		"title": "Biology",
		"department": "Science",
		"grades": (9,),
		"period": 2,
		"roster_size": 24,
		"teachers": ("elena.martinez", "samuel.price", "mei-lin.chen"),
		"focus": "cell biology, genetics, evolution, ecology, and evidence-based laboratory practice",
	},
	{
		"code": "SCI-CH-03",
		"title": "Chemistry",
		"department": "Science",
		"grades": (10, 11),
		"period": 3,
		"roster_size": 23,
		"teachers": ("samuel.price", "mei-lin.chen", "natalie.foster"),
		"focus": "atomic structure, reactions, stoichiometry, energy, and quantitative laboratory work",
	},
	{
		"code": "SCI-PH-04",
		"title": "Physics",
		"department": "Science",
		"grades": (11, 12),
		"period": 4,
		"roster_size": 21,
		"teachers": ("mei-lin.chen", "marcus.green", "samuel.price"),
		"focus": "mechanics, energy, waves, electricity, engineering design, and experimental analysis",
	},
	{
		"code": "SCI-ES-05",
		"title": "Environmental Science",
		"department": "Science",
		"grades": (10, 11, 12),
		"period": 5,
		"roster_size": 25,
		"teachers": ("elena.martinez", "natalie.foster", "marcus.green"),
		"focus": "ecosystems, climate systems, resource management, and community-based field research",
	},
	{
		"code": "SOC-WH-06",
		"title": "World History",
		"department": "Social Studies",
		"grades": (9, 10),
		"period": 6,
		"roster_size": 22,
		"teachers": ("thomas.nguyen", "grace.kim", "hannah.patel"),
		"focus": "global civilizations, primary-source analysis, historical argument, and civic perspective",
	},
	{
		"code": "SOC-US-07",
		"title": "United States History",
		"department": "Social Studies",
		"grades": (11,),
		"period": 7,
		"roster_size": 23,
		"teachers": ("david.cooper", "michael.turner", "thomas.nguyen"),
		"focus": "United States history through multiple perspectives, research, and document analysis",
	},
	{
		"code": "SOC-GE-01",
		"title": "Government and Economics",
		"department": "Social Studies",
		"grades": (12,),
		"period": 1,
		"roster_size": 20,
		"teachers": ("grace.kim", "david.cooper", "michael.turner"),
		"focus": "constitutional government, public policy, markets, personal finance, and civic participation",
	},
	{
		"code": "CSE-FD-02",
		"title": "Computer Science Foundations",
		"department": "Computer Science",
		"grades": (9, 10, 11, 12),
		"period": 2,
		"roster_size": 25,
		"teachers": ("victor.chen", "maya.singh", "christopher.hall"),
		"focus": "computational thinking, Python programming, data, algorithms, and responsible technology",
	},
	{
		"code": "CSE-AP-03",
		"title": "AP Computer Science A",
		"department": "Computer Science",
		"grades": (11, 12),
		"period": 3,
		"roster_size": 21,
		"teachers": ("victor.chen", "christopher.hall", "noah.williams"),
		"focus": "object-oriented programming, algorithms, data structures, and AP exam preparation",
	},
	{
		"code": "LAN-S1-04",
		"title": "Spanish I",
		"department": "World Languages",
		"grades": (9, 10),
		"period": 4,
		"roster_size": 24,
		"teachers": ("sofia.alvarez", "javier.morales", "hannah.patel"),
		"focus": "foundational communication, cultural literacy, listening, reading, and everyday conversation",
	},
	{
		"code": "LAN-S2-05",
		"title": "Spanish II",
		"department": "World Languages",
		"grades": (10, 11),
		"period": 5,
		"roster_size": 22,
		"teachers": ("javier.morales", "isabel.rivera", "sofia.alvarez"),
		"focus": "intermediate conversation, grammar in context, cultural inquiry, and authentic texts",
	},
	{
		"code": "ART-VD-06",
		"title": "Visual Arts and Design",
		"department": "Arts",
		"grades": (9, 10, 11, 12),
		"period": 6,
		"roster_size": 20,
		"teachers": ("emily.carter", "lila.thompson", "rachel.stein"),
		"focus": "drawing, composition, visual communication, design critique, and portfolio development",
	},
)

STUDENT_FIRST_NAMES = (
	"Aaliyah",
	"Abigail",
	"Adrian",
	"Aiden",
	"Alexa",
	"Alice",
	"Amelia",
	"Andrew",
	"Aria",
	"Audrey",
	"Benjamin",
	"Caleb",
	"Cameron",
	"Carlos",
	"Charlotte",
	"Chloe",
	"Daniel",
	"David",
	"Diego",
	"Eleanor",
	"Elijah",
	"Ella",
	"Emily",
	"Emma",
	"Ethan",
	"Evelyn",
	"Gabriel",
	"Grace",
	"Hannah",
	"Harper",
	"Henry",
	"Isabella",
	"Jack",
	"Jackson",
	"Jacob",
	"James",
	"Jasmine",
	"Jayden",
	"Joseph",
	"Julia",
	"Julian",
	"Layla",
	"Leo",
	"Liam",
	"Lily",
	"Lucas",
	"Lucy",
	"Mateo",
	"Maya",
	"Mia",
	"Naomi",
	"Noah",
	"Nora",
	"Olivia",
	"Owen",
	"Samuel",
	"Sofia",
	"Sophia",
	"Victoria",
	"William",
)

STUDENT_LAST_NAMES = (
	"Anderson",
	"Baker",
	"Bennett",
	"Brooks",
	"Brown",
	"Campbell",
	"Carter",
	"Chen",
	"Clark",
	"Collins",
	"Cooper",
	"Davis",
	"Diaz",
	"Edwards",
	"Evans",
	"Flores",
	"Foster",
	"Garcia",
	"Green",
	"Gupta",
	"Hall",
	"Harris",
	"Hernandez",
	"Hughes",
	"Jackson",
	"Johnson",
	"Kim",
	"Lee",
	"Lewis",
	"Li",
	"Lopez",
	"Martin",
	"Martinez",
	"Miller",
	"Mitchell",
	"Moore",
	"Morgan",
	"Murphy",
	"Nguyen",
	"Ortiz",
	"Parker",
	"Patel",
	"Perez",
	"Ramirez",
	"Reed",
	"Rivera",
	"Robinson",
	"Rodriguez",
	"Ross",
	"Sanchez",
	"Singh",
	"Smith",
	"Taylor",
	"Thomas",
	"Thompson",
	"Turner",
	"Walker",
	"Wang",
	"White",
	"Williams",
)


def _slug(value: str) -> str:
	return re.sub(r"[^a-z0-9]+", ".", value.lower()).strip(".")


def _build_teachers() -> list[dict]:
	return [
		{
			**teacher,
			"full_name": f"{teacher['first_name']} {teacher['last_name']}",
			"email": f"{teacher['key']}@staff.stanfordhigh.example",
		}
		for teacher in TEACHERS
	]


def _build_students() -> list[dict]:
	students = []
	name_count = len(STUDENT_FIRST_NAMES)
	for index in range(120):
		first_name = STUDENT_FIRST_NAMES[index % name_count]
		last_index = (index * 17 + (index // name_count) * 7) % len(STUDENT_LAST_NAMES)
		last_name = STUDENT_LAST_NAMES[last_index]
		if first_name.lower() == last_name.lower():
			last_name = STUDENT_LAST_NAMES[(last_index + 1) % len(STUDENT_LAST_NAMES)]

		grade = 9 + index // 30
		graduation_year = 2039 - grade
		email = f"{_slug(first_name)}.{_slug(last_name)}{graduation_year}" "@students.stanfordhigh.example"
		students.append(
			{
				"student_id": f"SHS-{index + 1:04d}",
				"first_name": first_name,
				"last_name": last_name,
				"full_name": f"{first_name} {last_name}",
				"email": email,
				"grade": grade,
				"graduation_year": graduation_year,
			}
		)
	return students


def _select_roster(students: list[dict], grades: tuple[int, ...], size: int, class_index: int) -> list[dict]:
	eligible = [student for student in students if student["grade"] in grades]
	start = (class_index * 11) % len(eligible)
	step = 7
	roster = []
	for offset in range(size):
		roster.append(eligible[(start + offset * step) % len(eligible)])
	return roster


def build_dataset() -> dict:
	"""Return the complete deterministic dataset without writing to the database."""
	teachers = _build_teachers()
	students = _build_students()
	teachers_by_key = {teacher["key"]: teacher for teacher in teachers}
	classes = []

	for index, spec in enumerate(CLASS_SPECS):
		start_time, end_time = PERIODS[spec["period"]]
		roster = _select_roster(students, spec["grades"], spec["roster_size"], index)
		classes.append(
			{
				**spec,
				"school": SCHOOL_NAME,
				"academic_year": ACADEMIC_YEAR,
				"course_title": f"{SCHOOL_NAME} - {spec['title']}",
				"batch_title": (
					f"{SCHOOL_NAME} - {spec['title']} - Period {spec['period']} ({ACADEMIC_YEAR})"
				),
				"teacher_emails": [teachers_by_key[key]["email"] for key in spec["teachers"]],
				"student_emails": [student["email"] for student in roster],
				"start_time": start_time,
				"end_time": end_time,
			}
		)

	return {
		"school": SCHOOL_NAME,
		"academic_year": ACADEMIC_YEAR,
		"start_date": START_DATE,
		"end_date": END_DATE,
		"timezone": TIMEZONE,
		"synthetic_data_notice": SYNTHETIC_DATA_NOTICE,
		"teachers": teachers,
		"students": students,
		"classes": classes,
	}


def preview() -> dict:
	"""Return a compact summary suitable for ``bench execute`` output."""
	dataset = build_dataset()
	student_load = Counter(
		email for class_record in dataset["classes"] for email in class_record["student_emails"]
	)
	return {
		"school": dataset["school"],
		"academic_year": dataset["academic_year"],
		"synthetic_data_notice": dataset["synthetic_data_notice"],
		"teachers": len(dataset["teachers"]),
		"students": len(dataset["students"]),
		"classes": len(dataset["classes"]),
		"class_sizes": {
			class_record["code"]: len(class_record["student_emails"]) for class_record in dataset["classes"]
		},
		"total_class_enrollments": sum(len(record["student_emails"]) for record in dataset["classes"]),
		"minimum_classes_per_student": min(student_load.values()),
		"maximum_classes_per_student": max(student_load.values()),
	}


def _ensure_category(category: str) -> None:
	if not frappe.db.exists("LMS Category", category):
		frappe.get_doc({"doctype": "LMS Category", "category": category}).insert(ignore_permissions=True)


def _ensure_user(record: dict, roles: tuple[str, ...]) -> bool:
	existing = frappe.db.exists("User", record["email"])
	user = frappe.get_doc("User", existing) if existing else frappe.new_doc("User")
	user.update(
		{
			"email": record["email"],
			"first_name": record["first_name"],
			"last_name": record["last_name"],
			"full_name": record["full_name"],
			"enabled": 1,
			"user_type": "Website User",
			"send_welcome_email": False,
		}
	)
	existing_roles = {row.role for row in user.roles}
	for role in roles:
		if role not in existing_roles:
			user.append("roles", {"role": role})
	user.save(ignore_permissions=True)
	return not bool(existing)


def _ensure_course(class_record: dict) -> tuple[str, bool]:
	existing = frappe.db.exists("LMS Course", {"title": class_record["course_title"]})
	course = frappe.get_doc("LMS Course", existing) if existing else frappe.new_doc("LMS Course")
	course.update(
		{
			"title": class_record["course_title"],
			"short_introduction": f"{class_record['title']} for the {ACADEMIC_YEAR} academic year.",
			"description": (
				f"An English-language {class_record['department']} course at {SCHOOL_NAME} focused on "
				f"{class_record['focus']}. {SYNTHETIC_DATA_NOTICE}"
			),
			"category": class_record["department"],
			"tags": f"{SCHOOL_NAME}, {class_record['department']}, {ACADEMIC_YEAR}, Synthetic Demo",
			"published": 1,
			"card_gradient": "Blue",
			"instructors": [{"instructor": email} for email in class_record["teacher_emails"]],
		}
	)
	course.save(ignore_permissions=True)
	return course.name, not bool(existing)


def _ensure_batch(class_record: dict, course_name: str) -> tuple[str, bool]:
	existing = frappe.db.exists("LMS Batch", {"title": class_record["batch_title"]})
	batch = frappe.get_doc("LMS Batch", existing) if existing else frappe.new_doc("LMS Batch")
	batch.update(
		{
			"title": class_record["batch_title"],
			"start_date": START_DATE,
			"end_date": END_DATE,
			"start_time": class_record["start_time"],
			"end_time": class_record["end_time"],
			"timezone": TIMEZONE,
			"medium": "Offline",
			"seat_count": len(class_record["student_emails"]),
			"description": (
				f"{class_record['code']} · Period {class_record['period']} · Grades "
				f"{', '.join(str(grade) for grade in class_record['grades'])}"
			),
			"batch_details": (
				f"<p>{class_record['focus'].capitalize()}.</p>"
				f"<p><strong>Demo notice:</strong> {SYNTHETIC_DATA_NOTICE}</p>"
			),
			"published": 0,
			"instructors": [{"instructor": email} for email in class_record["teacher_emails"]],
			"courses": [{"course": course_name}],
		}
	)
	batch.save(ignore_permissions=True)
	frappe.db.set_value("LMS Batch", batch.name, "published", 1, update_modified=False)
	return batch.name, not bool(existing)


def _ensure_course_enrollment(student_email: str, batch_name: str, course_name: str) -> None:
	filters = {"member": student_email, "course": course_name}
	existing = frappe.db.exists("LMS Enrollment", filters)
	course_enrollment = (
		frappe.get_doc("LMS Enrollment", existing) if existing else frappe.new_doc("LMS Enrollment")
	)
	course_enrollment.update(
		{
			"member": student_email,
			"course": course_name,
			"enrollment_from_batch": batch_name,
		}
	)
	course_enrollment.save(ignore_permissions=True)


def _ensure_batch_enrollment(student_email: str, batch_name: str, course_name: str) -> bool:
	filters = {"member": student_email, "batch": batch_name}
	if frappe.db.exists("LMS Batch Enrollment", filters):
		_ensure_course_enrollment(student_email, batch_name, course_name)
		return False

	enrollment = frappe.new_doc("LMS Batch Enrollment")
	enrollment.update(
		{
			"member": student_email,
			"member_name": frappe.db.get_value("User", student_email, "full_name"),
			"batch": batch_name,
			"confirmation_email_sent": 1,
		}
	)
	# This opt-in CLI seed deliberately avoids enrollment emails and does not
	# impersonate an Administrator. Insert the deterministic batch membership,
	# then save the linked LMS Enrollment through its normal model validation.
	enrollment.db_insert()
	_ensure_course_enrollment(student_email, batch_name, course_name)
	return True


def validate_seed() -> dict:
	"""Verify that the database matches the complete synthetic dataset."""
	dataset = build_dataset()
	errors = []
	total_batch_enrollments = 0
	total_course_enrollments = 0

	for class_record in dataset["classes"]:
		course_name = frappe.db.exists("LMS Course", {"title": class_record["course_title"]})
		batch_name = frappe.db.exists("LMS Batch", {"title": class_record["batch_title"]})
		expected_students = len(class_record["student_emails"])

		if not course_name:
			errors.append(f"Missing course: {class_record['course_title']}")
			continue
		if not batch_name:
			errors.append(f"Missing class: {class_record['batch_title']}")
			continue

		course_instructors = frappe.db.count(
			"Course Instructor", {"parent": course_name, "parenttype": "LMS Course"}
		)
		batch_instructors = frappe.db.count(
			"Course Instructor", {"parent": batch_name, "parenttype": "LMS Batch"}
		)
		batch_enrollments = frappe.db.count("LMS Batch Enrollment", {"batch": batch_name})
		course_enrollments = frappe.db.count(
			"LMS Enrollment",
			{
				"course": course_name,
				"enrollment_from_batch": batch_name,
			},
		)
		total_batch_enrollments += batch_enrollments
		total_course_enrollments += course_enrollments

		if course_instructors != 3:
			errors.append(f"{class_record['code']} course has {course_instructors} instructors, expected 3")
		if batch_instructors != 3:
			errors.append(f"{class_record['code']} class has {batch_instructors} instructors, expected 3")
		if batch_enrollments != expected_students:
			errors.append(
				f"{class_record['code']} has {batch_enrollments} batch enrollments, "
				f"expected {expected_students}"
			)
		if course_enrollments != expected_students:
			errors.append(
				f"{class_record['code']} has {course_enrollments} course enrollments, "
				f"expected {expected_students}"
			)

	if errors:
		frappe.throw(_("Stanford High School seed validation failed:") + "<br>" + "<br>".join(errors))

	return {
		"valid": True,
		"classes": len(dataset["classes"]),
		"teachers": len(dataset["teachers"]),
		"students": len(dataset["students"]),
		"batch_enrollments": total_batch_enrollments,
		"course_enrollments": total_course_enrollments,
	}


def seed() -> dict:
	"""Create or update the Stanford High School sample dataset.

	The operation is idempotent. Existing synthetic records are updated and
	missing records are created. No welcome or enrollment emails are sent.
	"""
	dataset = build_dataset()
	summary = {
		**preview(),
		"teachers_created": 0,
		"students_created": 0,
		"courses_created": 0,
		"classes_created": 0,
		"batch_enrollments_created": 0,
	}

	try:
		for category in sorted({record["department"] for record in dataset["classes"]}):
			_ensure_category(category)

		for teacher in dataset["teachers"]:
			summary["teachers_created"] += int(_ensure_user(teacher, ("Course Creator",)))

		for student in dataset["students"]:
			summary["students_created"] += int(_ensure_user(student, ("LMS Student",)))

		for class_record in dataset["classes"]:
			course_name, course_created = _ensure_course(class_record)
			summary["courses_created"] += int(course_created)
			batch_name, batch_created = _ensure_batch(class_record, course_name)
			summary["classes_created"] += int(batch_created)
			for student_email in class_record["student_emails"]:
				summary["batch_enrollments_created"] += int(
					_ensure_batch_enrollment(student_email, batch_name, course_name)
				)

		summary["verification"] = validate_seed()
		frappe.db.commit()
		return summary
	except Exception:
		frappe.db.rollback()
		raise
