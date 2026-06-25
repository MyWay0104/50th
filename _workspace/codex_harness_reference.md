# Codex Harness Reference

## 문제 분석

사용자는 새 주제 PPT 생성에 `MyWay0104/codex_harness.git` 활용을 요구했다.

## 설계

외부 repository는 `_workspace/codex_harness_reference/`에 shallow clone으로 보관한다. 실제 실행 harness는 이 프로젝트 내부 파일에 둔다.

## 구현

참조:

- Repository: `https://github.com/MyWay0104/codex_harness.git`
- 확인된 HEAD: `e4a2b4b28d222bfa96fc8080b4d93b07ce2e4bd8`
- Local clone: `_workspace/codex_harness_reference/`

## 코드

검증:

```powershell
python scripts\validate_codex_port.py
```

## 테스트 방법

`.codex/agents/*.toml`, `.agents/skills/**/SKILL.md`, `_workspace/orchestration-plan.md`가 존재하고 검증을 통과해야 한다.

## 향후 개선사항

참조 harness 업데이트가 필요하면 clone을 갱신하고, project-local harness와 차이를 audit한다.
