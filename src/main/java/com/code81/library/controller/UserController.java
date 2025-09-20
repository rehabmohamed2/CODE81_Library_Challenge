package com.code81.library.controller;

import com.code81.library.entity.Role;
import com.code81.library.entity.User;
import com.code81.library.entity.UserActivity;
import com.code81.library.repository.RoleRepository;
import com.code81.library.repository.UserRepository;
import com.code81.library.repository.UserActivityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired private UserRepository repo;
    @Autowired private RoleRepository roleRepository;
    @Autowired private UserActivityRepository activityRepository;
    @Autowired private PasswordEncoder passwordEncoder;

    @GetMapping
    public List<User> getAll() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<User> getById(@PathVariable Long id) {
        Optional<User> user = repo.findById(id);
        if (user.isPresent()) {
            return ResponseEntity.ok(user.get());
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public ResponseEntity<User> create(@RequestBody CreateUserRequest request) {
        try {
            if (repo.findByUsername(request.getUsername()).isPresent()) {
                return ResponseEntity.status(400).build();
            }

            User user = new User();
            user.setUsername(request.getUsername());
            user.setPassword(passwordEncoder.encode(request.getPassword()));

            Role role = roleRepository.findByName(request.getRoleName());
            if (role != null) {
                Set<Role> roles = new HashSet<>();
                roles.add(role);
                user.setRoles(roles);
            } else {
                return ResponseEntity.status(400).build();
            }

            User savedUser = repo.save(user);
            return ResponseEntity.ok(savedUser);
        } catch (Exception e) {
            return ResponseEntity.status(500).build();
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<User> update(@PathVariable Long id, @RequestBody UpdateUserRequest request) {
        Optional<User> optionalUser = repo.findById(id);
        if (optionalUser.isPresent()) {
            User user = optionalUser.get();

            if (request.getUsername() != null) {
                user.setUsername(request.getUsername());
            }

            if (request.getPassword() != null) {
                user.setPassword(passwordEncoder.encode(request.getPassword()));
            }

            if (request.getRoleName() != null) {
                Role role = roleRepository.findByName(request.getRoleName());
                if (role != null) {
                    Set<Role> roles = new HashSet<>();
                    roles.add(role);
                    user.setRoles(roles);
                }
            }

            User updatedUser = repo.save(user);
            return ResponseEntity.ok(updatedUser);
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

    @GetMapping("/{id}/activities")
    public ResponseEntity<List<UserActivity>> getUserActivities(@PathVariable Long id) {
        List<UserActivity> activities = activityRepository.findByUserIdOrderByTimestampDesc(id);
        return ResponseEntity.ok(activities);
    }

    public static class CreateUserRequest {
        private String username;
        private String password;
        private String roleName;

        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getPassword() { return password; }
        public void setPassword(String password) { this.password = password; }
        public String getRoleName() { return roleName; }
        public void setRoleName(String roleName) { this.roleName = roleName; }
    }

    public static class UpdateUserRequest {
        private String username;
        private String password;
        private String roleName;

        public String getUsername() { return username; }
        public void setUsername(String username) { this.username = username; }
        public String getPassword() { return password; }
        public void setPassword(String password) { this.password = password; }
        public String getRoleName() { return roleName; }
        public void setRoleName(String roleName) { this.roleName = roleName; }
    }
}