package com.code81.library.controller;

import com.code81.library.entity.Member;
import com.code81.library.repository.MemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/members")
public class MemberController {
    @Autowired private MemberRepository repo;

    @GetMapping
    public List<Member> getAll() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<Member> getById(@PathVariable Long id) {
        Optional<Member> member = repo.findById(id);
        if (member.isPresent()) {
            return ResponseEntity.ok(member.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public Member create(@RequestBody Member member) { return repo.save(member); }

    @PutMapping("/{id}")
    public ResponseEntity<Member> update(@PathVariable Long id, @RequestBody Member memberDetails) {
        Optional<Member> optionalMember = repo.findById(id);
        if (optionalMember.isPresent()) {
            Member member = optionalMember.get();
            member.setName(memberDetails.getName());
            member.setEmail(memberDetails.getEmail());
            member.setPhone(memberDetails.getPhone());
            member.setAddress(memberDetails.getAddress());
            member.setMembershipNumber(memberDetails.getMembershipNumber());
            member.setMembershipStartDate(memberDetails.getMembershipStartDate());
            member.setMembershipExpiryDate(memberDetails.getMembershipExpiryDate());
            member.setIsActive(memberDetails.getIsActive());
            Member updatedMember = repo.save(member);
            return ResponseEntity.ok(updatedMember);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        if (repo.existsById(id)) {
            repo.deleteById(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
