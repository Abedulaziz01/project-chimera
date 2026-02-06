setup:
	docker build -t chimera .

test:
	docker run chimera

spec-check:
	@echo "Spec check placeholder"
