from collections import Counter
from unittest import TestCase

from lms.demo.stanford_high_school import build_dataset, preview


class TestStanfordHighSchoolDataset(TestCase):
	def setUp(self):
		self.dataset = build_dataset()

	def test_dataset_has_expected_school_population(self):
		self.assertEqual(self.dataset["school"], "Stanford High School")
		self.assertEqual(len(self.dataset["classes"]), 20)
		self.assertEqual(len(self.dataset["teachers"]), 29)
		self.assertEqual(len(self.dataset["students"]), 120)

	def test_every_class_has_three_teachers_and_twenty_to_twenty_five_students(self):
		for class_record in self.dataset["classes"]:
			with self.subTest(class_code=class_record["code"]):
				self.assertEqual(len(class_record["teacher_emails"]), 3)
				self.assertEqual(len(set(class_record["teacher_emails"])), 3)
				self.assertGreaterEqual(len(class_record["student_emails"]), 20)
				self.assertLessEqual(len(class_record["student_emails"]), 25)
				self.assertEqual(
					len(class_record["student_emails"]), len(set(class_record["student_emails"]))
				)

	def test_people_are_unique_and_use_reserved_example_domains(self):
		people = self.dataset["teachers"] + self.dataset["students"]
		emails = [person["email"] for person in people]
		student_names = [student["full_name"] for student in self.dataset["students"]]
		self.assertEqual(len(emails), len(set(emails)))
		self.assertEqual(len(student_names), len(set(student_names)))
		self.assertTrue(all(email.endswith(".example") for email in emails))

	def test_rosters_only_include_students_from_the_allowed_grades(self):
		students_by_email = {student["email"]: student for student in self.dataset["students"]}
		for class_record in self.dataset["classes"]:
			with self.subTest(class_code=class_record["code"]):
				grades = {students_by_email[email]["grade"] for email in class_record["student_emails"]}
				self.assertTrue(grades.issubset(set(class_record["grades"])))

	def test_preview_matches_full_dataset(self):
		summary = preview()
		loads = Counter(email for record in self.dataset["classes"] for email in record["student_emails"])
		self.assertEqual(summary["classes"], 20)
		self.assertEqual(len(loads), len(self.dataset["students"]))
		self.assertEqual(summary["total_class_enrollments"], sum(loads.values()))
		self.assertEqual(summary["minimum_classes_per_student"], min(loads.values()))
		self.assertEqual(summary["maximum_classes_per_student"], max(loads.values()))
